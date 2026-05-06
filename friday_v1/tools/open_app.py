from tools.app_registry import get_app_path
from tools.open_website import run as open_website
import subprocess
import os


def run(target, memory):

    path = get_app_path(target)

    # If app not found → open as website
    if not path:
        return open_website(target, memory)

    try:

        if path.startswith("shell:"):
            subprocess.Popen(["explorer.exe", path])

        elif os.path.exists(path):
            subprocess.Popen(path)

        else:
            return open_website(target, memory)

        memory.set("last_app", target)

        return f"Opening {target}"

    except Exception as e:

        print("[DEBUG] Launch error:", e)

        return open_website(target, memory)