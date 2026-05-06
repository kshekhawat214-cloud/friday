import json
import os

ALIASES_FILE = "data/user_aliases.json"

DEFAULT_ALIASES = {
    "you tube": "youtube",
    "you to": "youtube",
    "riot luncher": "riot launcher",
    "visual studio": "vs code",
    "v s code": "vs code"
}

def load_aliases():
    if os.path.exists(ALIASES_FILE):
        with open(ALIASES_FILE, "r") as f:
            return json.load(f)
    return {}

def normalize_command(command):

    command = command.lower()

    aliases = load_aliases()

    merged_aliases = {**DEFAULT_ALIASES, **aliases}

    for wrong, correct in merged_aliases.items():
        command = command.replace(wrong, correct)

    return command