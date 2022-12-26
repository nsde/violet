import colorama

from . import gpt
from . import helpers
from . import sandbox

CODE_START = '```\n'
CODE_END = '\n```'

history = open('violet/model.txt').read().replace('#OS#', helpers.opsys)

def respond(prompt: str) -> str:
    global history
    response = gpt.generate(history=history, prompt=prompt)
    
    if CODE_START in response and CODE_END in response:
        code = response.split(CODE_START)[1].split(CODE_END)[0]
        response = sandbox.run(code)

        if response['status'] == 'success':
            colored = colorama.Fore.GREEN + response['message']
        else:
            colored = colorama.Fore.RED + response['message']

        response = response['message']
    else:
        colored = colorama.Fore.YELLOW + response

    history += \
f"""
Human: {prompt}
AI: {response}
"""

    return {
        'plain': response,
        'colored': colored 
    }

