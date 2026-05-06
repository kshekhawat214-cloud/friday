import os
import json
import subprocess
import win32com.client

REGISTRY_FILE = "data/app_registry.json"

app_registry = {}

IGNORE_EXE = [
    "service",
    "services",
    "helper",
    "updater",
    "installer",
    "crash",
    "report",
    "telemetry"
]

aliases = {
    "riot": "valorant",
    "riot client": "valorant",
    "riot launcher": "valorant",
    "chrome browser": "chrome",
    "browser": "chrome"
}



def resolve_shortcut(path):

    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        return shortcut.Targetpath
    except:
        return None


def register_app(name, path):

    name = name.lower().replace(".exe", "").strip()

    # prefer shorter paths (usually main launcher)
    if name not in app_registry or len(path) < len(app_registry[name]):
        app_registry[name] = path


def scan_start_menu():

    paths = [
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs")
    ]

    for base in paths:

        if not os.path.exists(base):
            continue

        for root, dirs, files in os.walk(base):

            for file in files:

                if file.endswith(".lnk"):

                    full = os.path.join(root, file)

                    target = resolve_shortcut(full)

                    if target and target.endswith(".exe"):
                        register_app(file.replace(".lnk",""), target)


def scan_desktop():

    desktop = os.path.expanduser(r"~\Desktop")

    if not os.path.exists(desktop):
        return

    for file in os.listdir(desktop):

        if file.endswith(".lnk"):

            full = os.path.join(desktop, file)

            target = resolve_shortcut(full)

            if target and target.endswith(".exe"):
                register_app(file.replace(".lnk",""), target)


def scan_program_files():

    bases = [
        r"C:\Program Files",
        r"C:\Program Files (x86)",
        os.path.expanduser(r"~\AppData\Local"),
        os.path.expanduser(r"~\AppData\Roaming")
    ]

    for base in bases:

        if not os.path.exists(base):
            continue

        try:

            for root, dirs, files in os.walk(base):

                for file in files:

                    if file.endswith(".exe"):   

                        name = file.replace(".exe", "").lower()

                        if any(word in name for word in IGNORE_EXE):
                            continue

                        exe = os.path.join(root, file)

                        register_app(name, exe)

                # limit scan depth
                if root.count(os.sep) - base.count(os.sep) > 2:
                    dirs[:] = []

        except PermissionError:
            continue


def scan_uwp_apps():

    try:

        output = subprocess.check_output(
            'powershell "Get-StartApps"',
            shell=True
        ).decode()

        for line in output.splitlines()[3:]:

            parts = line.strip().split()

            if len(parts) > 1:

                name = " ".join(parts[:-1]).lower()
                app_id = parts[-1]

                path = f"shell:AppsFolder\\{app_id}"

                register_app(name, path)

    except:
        pass


def full_scan():

    print("Running full application scan...")

    scan_start_menu()
    scan_desktop()
    scan_program_files()
    scan_uwp_apps()

    print(f"Detected {len(app_registry)} applications")


def quick_scan():

    print("Running quick scan for new apps...")

    scan_start_menu()
    scan_desktop()


def save_registry():

    os.makedirs("data", exist_ok=True)

    with open(REGISTRY_FILE, "w") as f:
        json.dump(app_registry, f, indent=4)


def load_registry():

    global app_registry

    try:

        with open(REGISTRY_FILE, "r") as f:
            app_registry = json.load(f)

        print(f"Loaded {len(app_registry)} apps from registry")

        return True

    except:
        return False


def build_registry():

    if load_registry():

        quick_scan()

    else:

        full_scan()

    save_registry()


def get_app_path(name):

    name = name.lower().strip()

    if name in aliases:
        name = aliases[name]

    if name in app_registry:
        return app_registry[name]

    for app, path in app_registry.items():
        if name in app:
            return path

    for app, path in app_registry.items():
        if app in name:
            return path

    return None