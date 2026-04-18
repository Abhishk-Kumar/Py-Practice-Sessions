import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "<Your Key Here>"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    print(f"DEBUG command received: '{c}'")  # pehle ye dekho console mein
    
    if "google" in c.lower():
        webbrowser.open("https://google.com")
    elif "facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        output = aiProcess(c)
        speak(output)





if __name__ == "__main__":
    speak_old("Initializing ass")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            
            word = r.recognize_google(audio)
            print(f"Heard: {word}")  # debug

            if "jarvis" in word.lower():  # ✅ substring match
                speak_old("Ya")           # ✅ instant response
                
                with sr.Microphone() as source:
                    print("Jarvis Active... Listening for command...")
                    audio = r.listen(source, timeout=10, phrase_time_limit=10)
                
                command = r.recognize_google(audio)
                print(f"Command: {command}")  # debug
                processCommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected, retrying...")
        except Exception as e:
            print(f"Error: {e}")

