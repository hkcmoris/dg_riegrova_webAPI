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

you need to create a file called `dg_riegrova_webapi.config.json` in the same directory as your script.

```json
{
  "baseurl": "http://www.skolka-riegrova.cz",
  "adminlogin": "/prihlaseni/",
  "admindashboard": "/admin/webstructadmin/show/"
}
```

I suggest you create .env file in the same directory as your script and store your admin credentials there.

```bash
ADMIN_USER="username"
ADMIN_PASS="password"
```

### Usage

```python
from dg_riegrova_webapi import RiegrovaWebAPI as api

api.init()
api.login(os.getenv('ADMIN_USER'), os.getenv('ADMIN_PASS'))
result = api.example_get_function()
api.example_post_function(data)
```
