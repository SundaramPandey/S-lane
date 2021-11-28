import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from plyer import notification

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! sir")   

    else:
        speak("Good Evening! sir")  

    speak("Hello I am S lane. how may i help you sir ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("listening...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said {query}\n")

    except Exception as e:
        print("please say that again")

        return "None"
    return query

speak("Please speak your name")
name = takeCommand()
speak("Please speak your gender as (m) for male and (f) for female and (t) for transgender")
gender = takeCommand()
       

def wish_male():
    hour = (datetime.datetime.now().hour)
    namem = f"Good morning {name} sir"
    nameam = f"Good Afternoon {name} sir"
    namepm = f"Good evening {name} sir"
    if hour >= 0 and hour < 12:
        speak(namem)
    if hour >= 12 and hour < 17:
        speak(nameam)
    else:
        speak(namepm)

def wish_female():
    hour = (datetime.datetime.now().hour)
    namef = f"Good morning {name} mam"
    namefm = f"Good after noon{name} mam"
    namepm = f"Good evening {name} mam"
    if hour >= 0 and hour < 12:
        speak(namef)
    if hour >= 12 and hour < 17:
        speak(namefm)
    else:
        speak(namepm)

def wish_transgender():
    hour = (datetime.datetime.now().hour)
    tm = f"Good morning {name}"
    ta = f"Good After noon {name}"
    te = f"Good evening {name}"
    if hour >= 0 and hour < 12:
        speak(tm)
    if hour >= 12 and hour < 17:
        speak(ta)
    else:
        speak(te)

if gender == "m":
    wish_male()

if gender == "f":
    wish_female()

if gender == "t":
    wish_transgender()

while gender != "m" or gender != "f" or gender != "t":
    speak("Please say that again")
    gender = takeCommand()
    if gender == "male" or gender == "female" or gender == "transgender":
       speak("ok")
       break

    while True:

        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
          webbrowser.open("youtube.com")

        elif "open google" in query:
          webbrowser.open("google.com")

        elif "open colab" in query:
          webbrowser.open("https://colab.research.google.com/")

        elif "open stackeoverflow" in query:
          webbrowser.open("stackeoverflow.com")
        
        elif "time" in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"sir The time is{strTime}")

        elif "open amazon" in query:
          webbrowser.open("amazon.com")

        elif "open flipkart" in query:
          webbrowser.open("https://www.flipkart.com/")

        elif "open angel broking" in query:
            webbrowser.open("https://www.angelone.in/")

        elif "open whatsapp" in query:
          webbrowser.open("https://web.whatsapp.com/")

        elif "open w3 schools python" in query:
          webbrowser.open("https://www.w3schools.com/python/")

        elif "open w3 schools html" in query:
          webbrowser.open("https://www.w3schools.com/html/")

        elif "brown munde" in query:
          music = "C:\\Users\\jitendra pandey\\Music\\music"
          songs = os.listdir(music)
          os.startfile(os.path.join(music, songs[0]))

        elif "despacito" in query:
          m = "C:\\Users\\jitendra pandey\\Music\\music"
          song1 = os.listdir(m)
          os.startfile(os.path.join(m, song1[1]))

        elif "send notification" in query:
          speak("What should I say in the notification")
          messages = takeCommand()
          print(messages)
          notification.notify(
                title="S-lane",
                message=messages,
               timeout=10
          )