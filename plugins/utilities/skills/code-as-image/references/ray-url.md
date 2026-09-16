# ray.so URL encoding

Read the snippet from a file or stdin rather than interpolating code into a shell command. Encode UTF-8 bytes as base64, then URL-encode the fragment values. For example:

```python
import base64
from pathlib import Path
from urllib.parse import urlencode

code = Path("snippet.txt").read_bytes()
params = {
    "code": base64.b64encode(code).decode("ascii"),
    "theme": "candy",
    "padding": "64",
    "darkMode": "true",
    "background": "true",
    "language": "auto",
}
url = "https://ray.so/#" + urlencode(params)
print(url)
```

The fragment preserves the literal snippet including trailing newlines. Inspect the live renderer and output; supported parameter values can change. Carbon uses a different URL schema and is not a drop-in substitution.
