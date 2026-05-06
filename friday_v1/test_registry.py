from tools.app_registry import scan_apps

apps = scan_apps()

print(list(apps.keys())[:20])