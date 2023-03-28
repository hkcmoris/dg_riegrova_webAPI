import logging
import os
import json


CONFIG = None
CONFIG_FILE_NAME = "dg_riegrova_webAPI.config.json"


def init():
    """Initialize the Riegrova Web API module.

    Returns
    -------
    bool
        True if the module was initialized successfully, False otherwise.
    """
    if not os.path.exists(CONFIG_FILE_NAME):
        error = f"Config file `{CONFIG_FILE_NAME}` not found. See README.md for more information."
        logging.error(error)
        print(error)
        return False

    with open(os.path.join(".", CONFIG_FILE_NAME), "r", encoding="utf-8") as configFile:
        global CONFIG
        CONFIG = json.load(configFile)

    # Check if the config file is valid
    if not CONFIG:
        error = f"Config file `{CONFIG_FILE_NAME}` is empty."
        logging.error(error)
        print(error)
        return False

    if "baseurl" not in CONFIG:
        error = f"Config file `{CONFIG_FILE_NAME}` does not contain a `baseurl` entry."
        logging.error(error)
        print(error)
        return False

    if "adminlogin" not in CONFIG:
        error = f"Config file `{CONFIG_FILE_NAME}` does not contain an `adminlogin` entry."
        logging.error(error)
        print(error)
        return False

    if "admindashboard" not in CONFIG:
        error = f"Config file `{CONFIG_FILE_NAME}` does not contain an `admindashboard` entry."
        logging.error(error)
        print(error)
        return False

    return True


def login(username, password):
    """Login to the Riegrova Web API.

    Parameters
    ----------
    username : str
        Username to login with.
    password : str
        Password to login with.

    Returns
    -------
    str
        The API token to use for future requests.
    """


if __name__ == '__main__':
    print('This is a module, not a program. Please import it instead.')
