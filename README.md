# DevGround

## Riegrova webAPI

This is a simple webAPI for the Riegrova webpage cms

### hosted on

http://www.skolka-riegrova.cz/

### Language

It is written in Python.

### License

It is licensed under the MIT license.

### Requirements

It requires the following python modules:

- beautifulsoup4
- MechanicalSoup

### Installation

install the package with pip:

```bash
pip install dg_riegrova_webapi
```

### Usage

```python
from dg_riegrova_webapi import RiegrovaWebAPI

api = RiegrovaWebAPI()
api.login("username", "password")
result = api.example_get_function()
api.example_post_function(data)
```
