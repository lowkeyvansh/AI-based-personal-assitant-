import speech_recognition as sr
import pyttsx3
import requests

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."

if __name__ == "__main__":
    while True:
        command = listen()
        if 'exit' in command:
            speak("Goodbye!")
            break
        
        response = requests.post('http://localhost:5000/process', json={'text': command}).json()
        speak(response['response'])
