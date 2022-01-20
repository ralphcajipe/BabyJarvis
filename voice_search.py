"""Perform a Google Search"""

import webbrowser
import speech_recognition as sr

speech = sr.Recognizer()


def voice_to_text():
    """Capture voice input and converts to text."""
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input


while True:
    print("I'm listening Sir...")
    inp = voice_to_text()
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print('Goodbye Sir.')
        break
    elif "google" in inp:
        inp = inp.replace('google ', '')
        webbrowser.open("https://google.com/search?q=" + inp)
        continue
