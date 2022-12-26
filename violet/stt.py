import speech_recognition as sr

recognizer = sr.Recognizer()

def ask() -> str:
    try:
        with sr.Microphone() as source2:
            recognizer.adjust_for_ambient_noise(source2, duration=1)
            recording = recognizer.listen(source2, timeout=5)
            return recognizer.recognize_google(recording, language='de-DE')
            
    except sr.RequestError:
        return 'I did not understand what you said.'

    except sr.UnknownValueError:
        return 'There was an error processing what you said.'
