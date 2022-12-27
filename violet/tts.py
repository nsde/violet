import os
import gtts
import playsound

from . import lang

def say(text: str) -> None:
    """Says a plain text using Google TTS."""
    tts = gtts.gTTS(text=text, lang=lang.detect(text)[0]) #, lang='en'
    filename = 'tts.temp.mp3'
    tts.save(filename)

    playsound.playsound(filename)
    os.remove(filename)
