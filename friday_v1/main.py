 from interface.wake_word import listen_for_wake_word
from interface.speech_to_text import listen
from interface.text_to_speech import speak

from brain.friday_brain import process_command
from brain.command_normalizer import normalize_command
from brain.logger import log_command

from tools.app_registry import build_registry
from tools.tool_manager import load_tools
from tools.system_monitor import monitor_system

import threading
import time


def main():

    print("Friday Starting...")

    # Build app registry
    build_registry()

    # Load tools
    load_tools()

    # Start system monitoring in background
    monitor_thread = threading.Thread(target=monitor_system, daemon=True)
    monitor_thread.start()

    speak("Friday online")

    while True:

        # Wait for wake word
        listen_for_wake_word()

        speak("Yes sir, how may I help you?")

        conversation_session()


def conversation_session():

    timeout = 10
    last_interaction = time.time()

    while True:

        command = listen()

        if not command:
            continue

        command = command.strip()

        # Silence timeout
        if command == "":
            if time.time() - last_interaction > timeout:
                speak("Okay. Call me if you need anything.")
                break
            continue

        print("You said:", command)

        # Normalize command (fix STT mistakes)
        command = normalize_command(command)

        # Log command
        log_command(command)

        # Process command through Friday brain
        response = process_command(command)

        # Speak response
        if response:
            speak(response)

        last_interaction = time.time()


if __name__ == "__main__":
    main()