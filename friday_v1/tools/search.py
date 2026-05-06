import webbrowser


def run(target, memory):

    last_app = memory.get("last_app")

    query = target.replace(" ", "+")

    if last_app == "youtube":

        url = f"https://www.youtube.com/results?search_query={query}"

    else:

        url = f"https://www.google.com/search?q={query}"

    memory.set("last_search", target)

    webbrowser.open(url)

    return f"Searching {last_app or 'Google'} for {target}"