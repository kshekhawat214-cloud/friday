import webbrowser

WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com"
}


def run(target, memory):

    target = target.lower().strip()

    if target in WEBSITES:
        url = WEBSITES[target]
    else:
        url = f"https://{target}.com"

    webbrowser.open(url)

    memory.set("last_app", target)

    return f"Opening {target}"