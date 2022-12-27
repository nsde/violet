import colorama
import speech_recognition

recognizer = speech_recognition.Recognizer()

def ask() -> str:
    try:
        with speech_recognition.Microphone() as source2:
            recognizer.adjust_for_ambient_noise(source2, duration=1)
            recording = recognizer.listen(source2, timeout=5)

            recognized_text = recognizer.recognize_google(recording, language='en-US') # lang.detect(text)[1]
            print(f'{colorama.Fore.BLUE}[STT] {recognized_text}')
            return recognized_text
            
    except speech_recognition.RequestError:
        return 'I did not understand what you said.'

    except speech_recognition.UnknownValueError:
        return 'There was an error processing what you said.'
