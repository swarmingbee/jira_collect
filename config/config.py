"""
Module responsible for creating of the conf
file and also the token
"""

import os
import json

# Setting the conf file
home_dir = os.path.expanduser("~")
CONF_FILE = home_dir + "/.jira_collect.conf"
DEFAULT_TOKEN = {"token": ""}


def read_token():
    """
    Def responsible for reading the conf file
    """

    try:
        with open (CONF_FILE, "r", encoding="utf-8") as file_ref:
            token_in_file = json.load(file_ref)

    except FileNotFoundError:
        print("Conf file not found! Please, set the token")
        with open(CONF_FILE, "w", encoding="utf-8") as file_ref:
            file_ref.write(json.dumps(DEFAULT_TOKEN))
        token_in_file = DEFAULT_TOKEN 

    return token_in_file['token']


def set_token():
    """
    Def responsible for create the conf file adding the token
    """
    print("setting token")
    input_token = input("Please, paste the JIRA token: ")

    aux = {"token": input_token}

    with open(CONF_FILE, "w", encoding="utf-8") as file_ref:
        file_ref.write(json.dumps(aux, indent=4))


def show_token():
    """
    Def responsible for show the content of the content file (token)
    """
    with open(CONF_FILE, "r", encoding="utf-8") as file_ref:
        print(json.dumps(json.load(file_ref), indent=4))
