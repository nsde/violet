import os
import gtts
import colorama
import playsound

from . import lang

def say(text: str) -> None:
    """Says a plain text using Google TTS."""
    # print(f'{colorama.Fore.YELLOW}[TTS] Detected language: {lang.detect(text)}')
    tts = gtts.gTTS(text=text, lang='en')
    filename = 'tts.temp.mp3'
    tts.save(filename)

    playsound.playsound(filename)
    os.remove(filename)
