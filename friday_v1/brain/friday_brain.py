from brain.intent_parser import parse_intent
from brain.command_router import route_command
from brain.command_splitter import split_commands
from brain.task_queue import task_queue
from memory.context_memory import context_memory


def process_command(command):

    commands = split_commands(command)

    # store last command
    if command not in ["repeat", "again", "do that again"]:
        context_memory.set("last_command", command)

    for cmd in commands:

        intent, target = parse_intent(cmd)

        task_queue.add(
            lambda intent=intent, target=target: route_command(
                intent,
                target,
                context_memory
            )
        )

    responses = task_queue.run()

    return " ".join(responses)