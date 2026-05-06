import os
import importlib
from brain.logger import log_tool, log_error

TOOLS = {}

def load_tools():

    tool_folder = "tools"

    for file in os.listdir(tool_folder):

        if file.endswith(".py") and file not in ["tool_manager.py", "__init__.py"]:

            module_name = file[:-3]

            try:
                module = importlib.import_module(f"tools.{module_name}")

                if hasattr(module, "run"):

                    TOOLS[module_name] = module.run

            except Exception as e:
                log_error(f"Failed loading tool {module_name}: {e}")

    print("Loaded tools:", list(TOOLS.keys()))


def execute_tool(tool_name, target, memory):

    if tool_name in TOOLS:

        try:
            log_tool(tool_name)
            return TOOLS[tool_name](target, memory)

        except Exception as e:
            log_error(f"Tool {tool_name} failed: {e}")
            return "Something went wrong while executing the command."

    return "Sorry, I don't know how to do that."