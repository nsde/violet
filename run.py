import sys
import colorama

import violet

colorama.init(autoreset=True)

if len(sys.argv) > 1:
    prompt = ' '.join(sys.argv[1:])
    print(violet.respond(prompt)['colored'])

else:
    while True:
        try:
            prompt = input(colorama.Fore.BLUE)
        except KeyboardInterrupt:
            sys.exit(0)

        print(colorama.Fore.RESET, end='')
        print(violet.respond(prompt)['colored'])
