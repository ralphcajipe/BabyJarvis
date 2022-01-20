"""Test SpeechRecognition"""

import speech_recognition as sr

speech = sr.Recognizer()
print("I'm listening Sir...")
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)
    inp = speech.recognize_google(audio)
print(f'You just said {inp}.')
