# Purpose
zlibrary is the world's largest collection if E-books and Articles available to the public for free. zlibrary_python is a Scrapper for the zlibrary website to make integration into other applications less painstaking. It strives to fast-track the development of tools that make knowledge more accessible. 

Repo also includes a flask API service in `./api`. It is live at [https://zlibrary-api.jb2k4.repl.co/](https://zlibrary-api.jb2k4.repl.co/) for the frontend friends.

# Usage
### Setup
```python
from zlibrary_python.a_sync import srape_search_query

import asyncio

loop = asyncio.get_event_loop()
print(loop.run_until_complete(srape_search_query('some query here. needn\'t be url encoded')))
loop.close()
```
set `fuzzy = True` in `srape_search_query` for getting the first 50 results that include fuzzy matches
### Output
```json
[
    ...
    {
        "title": "41 Years IIT JEE Mathematics",
        "url": "https://1lib.in/book/5630454/30bf56/",
        "downloadurl": "https://1lib.in/dl/5630454/30bf56/",
        "author": "Amit M Agarwal",
        "publisher": "Arihant",
        "year": 2020.0,
        "language": "english",
        "rating": {
            "interest": 0.0,
            "quality": 0.0
        }
    },
    ...
]
```
