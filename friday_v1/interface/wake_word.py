import pvporcupine
import pyaudio
import struct

ACCESS_KEY = "LnEz8DiyXAMIc+6uY+1G+9NYQk4y9UdeaEjDLd6CTSvIyKlAgv13PQ=="


def listen_for_wake_word():

    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=["models/friday.ppn"]
    )

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length,
    )

    print("Waiting for wake word...")

    while True:

        pcm = audio_stream.read(porcupine.frame_length)

        pcm = struct.unpack_from(
            "h" * porcupine.frame_length, pcm
        )

        result = porcupine.process(pcm)

        if result >= 0:
            print("Wake word detected!")
            return True