import asyncio
import edge_tts
import pygame
import uuid
import os

VOICE = "en-US-AriaNeural"


async def _speak_async(text):

    filename = f"voice_{uuid.uuid4()}.mp3"

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.unload()
    os.remove(filename)


def speak(text):

    print("Friday:", text)
    asyncio.run(_speak_async(text))