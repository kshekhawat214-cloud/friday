import speech_recognition as sr

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.8


def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,            # wait for speech
                phrase_time_limit=6   # max command length
            )

        except sr.WaitTimeoutError:

            # no speech detected
            return ""

    try:

        text = recognizer.recognize_google(audio)

        text = text.lower().strip()

        print("You said:", text)

        return text

    except sr.UnknownValueError:

        return ""

    except sr.RequestError:

        print("Speech service unavailable")
        return ""