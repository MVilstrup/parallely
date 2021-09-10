# Parallely - Parallel Python made simple

```python
from parallely import threaded
import requests

@threaded(max_workers=100)
def fetch_data(url):
    return requests.get(url).json()

>> fetch_data("http://www.SOME-WEBSITE.com/data/cool-stuff")
"{ Some data }"

>> fetch_data.map([
    "http://www.SOME-WEBSITE.com/data/cool-stuff",
    "http://www.SOME-WEBSITE.com/data/cool-stuff",
    "http://www.SOME-WEBSITE.com/data/cool-stuff"
])
"[{ Some data }, { Some data }, { Some data }]"
```