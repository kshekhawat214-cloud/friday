import json
import os

ALIASES_FILE = "data/user_aliases.json"

def save_alias(user_term, actual_app):

    if os.path.exists(ALIASES_FILE):
        with open(ALIASES_FILE, "r") as f:
            aliases = json.load(f)
    else:
        aliases = {}

    aliases[user_term] = actual_app

    with open(ALIASES_FILE, "w") as f:
        json.dump(aliases, f, indent=4)