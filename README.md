# ***V i o l e t G P T***
🤖 A next-generation chat bot based on OpenAI, which can access your files, open the webbrowser and more!

## Features
- Accurate mathematical calculations
- File system access
- Voice support (SpeechToText + TextToSpeech)
- Errors are explained

### Planned
- Start sandbox in another thread, detect print() stuff
- API access (save your API tokens for various services in a `.env` file, and the bot will be able to find out e.g. the weather.)
- Web UI planned (the sandbox has a way higher priority, though! No web UI is going to be worked on before there is no proper sandbox.)

## Warning
The sandbox is currently being developed, which means, in theory, the bot do anything.

Never, ever run the bot with administrator permissions. You should always make sure the sandbox can't delete any imporant files!
Additionally, never ever, give others access to the sandbox features! Malicious actors could use this as a remote code execution.

## Support
✅ Debian-Based GNU+Linux Distros (such as Mint 20.2)

✅ Windows 10 (and above)

✅ MacOS (probably - testers needed!)

***

✅ Python 3.8.10+

## Setup
1. Create a `.env` in *this* directory with the following content:
```
OPENAI_API_KEY=sk-ywvx6zhMxWDeQTL69LQMKoBz4Gr26QCAhF6xom9bWUHTuujF
```
2. Replace the value of `OPENAI_API_KEY` with your actual OpenAI API key. The API key above is just an example and doesn't work. Don't give anyone access to anything stored in your `.env`.

3. Then - assuming you already have *Python* and *pip* installed, run `pip install -r requirements.txt`

## Troubleshooting
### `AttributeError: Could not find PyAudio; check installation`
```
pip install pipwin
pipwin install pyaudio
```

Debian-based GNU+Linux:

```
sudo apt-get install python3-pyaudio
```

## Example tasks
- What WiFi am I connected with (on Linux)?
- Tell me a short story!
- Translate "Hello there" into Spanish!
