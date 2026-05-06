import webbrowser


def run(target, memory):

    last_app = memory.get("last_app")
    last_search = memory.get("last_search")

    if not last_search:
        return "You haven't searched anything yet."

    if last_app == "youtube":

        url = f"https://www.youtube.com/results?search_query={last_search.replace(' ','+')}"
        webbrowser.open(url)

        return "Opening the search results."

    return "I can't open results for that yet."