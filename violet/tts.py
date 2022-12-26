import os
import gtts
import playsound

def say(text):
    tts = gtts.gTTS(text=text, lang='de') #, lang='en'
    filename = 'tts.temp.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
