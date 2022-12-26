import colorama
import subprocess

from . import gpt

def run(code: str):
    print(colorama.Style.DIM + 'Launching sandbox...')
    with open('sandbox/_temp.py', 'w') as f:
        f.write(code)

    # output = subprocess.check_output(, stderr=subprocess.DEVNULL).decode('utf8').strip()
    process = subprocess.Popen(['python', 'sandbox/_temp.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    output = stdout.decode('utf8').strip()
    errors = stderr.decode('utf8').strip()

    if errors:
        return {
        'status': 'error',
        'message': gpt.explain_error(errors)
    }

    return {
        'status': 'success',
        'message': output
    }
