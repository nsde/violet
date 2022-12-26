import sys
import colorama
import playsound

import violet

colorama.init(autoreset=True)

while True:
    try:
        prompt = violet.ask()

    except KeyboardInterrupt:
        sys.exit(0)

    answer = violet.respond(prompt)
    print(answer['colored'])
    violet.say(answer['plain'])
