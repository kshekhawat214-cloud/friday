def parse_intent(command):

    command = command.lower()

    # OPEN APP
    open_words = ["open", "launch", "start", "run"]

    for word in open_words:
        if command.startswith(word):

            target = command.replace(word, "").strip()

            return "open_app", target

    # repeat command
    if command in ["repeat", "do that again", "again"]:
        return "repeat_command", None

    if command.startswith("open "):
        return "open_app", command.replace("open ", "")

    if command.startswith("search "):
        return "search", command.replace("search ", "")

    
    if command in ["another", "another one", "another search"]:
        return "another_search", None

    # SEARCH
    if command.startswith("search"):

        target = command.replace("search", "").strip()

        return "search", target

    # SHUTDOWN
    if "shutdown" in command or "turn off" in command:

        return "shutdown_pc", None

    # GREETING
    if "hello" in command or "hi" in command:

        return "greeting", None

    return "unknown", command