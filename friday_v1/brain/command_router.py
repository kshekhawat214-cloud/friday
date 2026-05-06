from tools.tool_manager import execute_tool
from brain.smart_matcher import match_app
from brain.logger import log_intent


def route_command(intent, target, memory):

    # repeat last command
    if intent == "repeat_command":

        last_command = memory.get("last_command")

        if not last_command:
            return "There is nothing to repeat."

        from brain.friday_brain import process_command

        return process_command(last_command)

    #last search
    if intent == "another_search":

        last_search = memory.get("last_search")

        if not last_search:
            return "There is no previous search."

        return execute_tool("search", last_search, memory)

    # open application
    if intent == "open_app":

        target = match_app(target)

        return execute_tool(intent, target, memory)

    log_intent(intent, target)

    # default tool execution
    return execute_tool(intent, target, memory)