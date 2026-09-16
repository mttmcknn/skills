#!/usr/bin/env ruby
# Run after overlaying this branch's Jekyll source onto the marketplace checkout.
# Only manifest-listed plugins are published. Support files remain on GitHub.
require 'fileutils'
require 'json'
require 'open3'
require 'pathname'
require 'yaml'

POSTS_DIR = '_posts'

def first_commit_date(path)
  out, status = Open3.capture2('git', 'log', '--follow', '--format=%cI', '--', path)
  return nil unless status.success?
  out.strip.split("\n").last&.split('T')&.first
end

def github_resource_links(body, skill_path, repository)
  fenced = false
  body.lines.map do |line|
    if line.match?(/^\s*```/)
      fenced = !fenced
      next line
    end
    next line if fenced
    line.gsub(/(\[[^\]]*\]\()([^\s)]+)(\))/) do
      prefix, target, suffix = Regexp.last_match.captures
      if target.match?(%r{\A(?:[a-zA-Z][a-zA-Z0-9+.-]*:|/|#)})
        "#{prefix}#{target}#{suffix}"
      else
        path, fragment = target.split('#', 2)
        resolved = Pathname.new(File.join(File.dirname(skill_path), path)).cleanpath.to_s
        raise "Missing resource: #{resolved}" unless File.exist?(resolved)
        raise "Resource escapes repository: #{resolved}" if resolved.start_with?('../')
        kind = File.directory?(resolved) ? 'tree' : 'blob'
        anchor = fragment ? "##{fragment}" : ''
        "#{prefix}https://github.com/#{repository}/#{kind}/main/#{resolved}#{anchor}#{suffix}"
      end
    end
  end.join
end

marketplace = JSON.parse(File.read('.claude-plugin/marketplace.json'))
config = YAML.safe_load(File.read('_config.yml'))
repository = "#{config.fetch('github').fetch('username')}/skills"
FileUtils.rm_rf(POSTS_DIR)
FileUtils.mkdir_p(POSTS_DIR)
count = 0
marketplace.fetch('plugins').each do |plugin|
  source = plugin.fetch('source')
  Dir.glob(File.join(source, 'skills', '*', 'SKILL.md')).sort.each do |path|
    raw = File.read(path)
    match = raw.match(/\A---\s*\n(.*?)\n---\s*\n/m)
    raise "Missing skill metadata: #{path}" unless match
    metadata = YAML.safe_load(match[1])
    body = raw[match.end(0)..-1].lstrip
    clean = body.gsub(/```[\s\S]*?```/, '')
    title = clean[/^# (.+)$/, 1] || metadata.fetch('name')
    date = first_commit_date(path) || Time.now.strftime('%Y-%m-%d')
    slug = metadata.fetch('name')
    name = plugin.fetch('name')
    frontmatter = {
      'layout' => 'post', 'title' => title.strip,
      'description' => metadata.fetch('description'), 'date' => date,
      'categories' => [name], 'tags' => [name, 'skill'],
      'permalink' => "/#{name}/skills/#{slug}/", 'toc' => true, 'pin' => false
    }
    body = github_resource_links(body, path, repository)
    File.write(File.join(POSTS_DIR, "#{date}-#{name}-#{slug}.md"),
               frontmatter.to_yaml + "---\n\n" + body)
    count += 1
  end
end
puts "Generated #{count} posts in #{POSTS_DIR}/"
