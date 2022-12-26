# ***V i o l e t G P T***
🤖 A next-generation chat bot based on OpenAI, which can access your files, open the webbrowser and more!

## Features
- Accurate mathematical calculations
- File system access
- Voice support (SpeechToText + TextToSpeech)
- Errors are explained

### Planned
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
- what wifi am I connected with on Linux
- 