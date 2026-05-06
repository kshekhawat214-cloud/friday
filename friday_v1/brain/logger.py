import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "friday.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_command(command):
    logging.info(f"COMMAND: {command}")

def log_intent(intent, target):
    logging.info(f"INTENT: {intent} | TARGET: {target}")

def log_tool(tool_name):
    logging.info(f"TOOL USED: {tool_name}")

def log_error(error):
    logging.error(f"ERROR: {error}")