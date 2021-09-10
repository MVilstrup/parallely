# Parallely - Parallel Python made simple

```python
from parallely import threaded
import requests

@threaded(max_workers=500)
def fetch_data(url):
    return requests.get(url).json()

# Use the function as usual for fine grained control, testing etc. 
fetch_data("http://www.SOME-WEBSITE.com/data/cool-stuff")

# Use a thread-pool to map over a list of inputs in concurrent manner
fetch_data.map([
    "http://www.SOME-WEBSITE.com/data/cool-stuff",
    "http://www.SOME-WEBSITE.com/data/cool-stuff",
    "http://www.SOME-WEBSITE.com/data/cool-stuff"
])
```