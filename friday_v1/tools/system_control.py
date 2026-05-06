import os

def run(target, memory):

    if target == "shutdown":

        os.system("shutdown /s /t 1")

        return "Shutting down your computer"

    return "Unknown system command"