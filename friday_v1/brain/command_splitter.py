def split_commands(text):

    separators = [
        " and ",
        " then ",
        " after that "
    ]

    commands = [text]

    for sep in separators:

        new_commands = []

        for cmd in commands:

            if sep in cmd:
                parts = cmd.split(sep)
                new_commands.extend(parts)
            else:
                new_commands.append(cmd)

        commands = new_commands

    return [cmd.strip() for cmd in commands if cmd.strip()]