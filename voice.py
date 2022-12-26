import sys
import colorama
import pyttsx3

import violet

colorama.init(autoreset=True)
engine = pyttsx3.init()

while True:
    try:
        prompt = input(colorama.Fore.BLUE)

    except KeyboardInterrupt:
        sys.exit(0)

    answer = violet.respond(prompt)
    print(answer['colored'])
    
    engine.say(answer['plain'])
    engine.runAndWait()
