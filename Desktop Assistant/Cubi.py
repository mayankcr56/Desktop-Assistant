import pyttsx3 #pip install pyttsx3
import datetime #
import speech_recognition as sr #pip install speechRecongnition
import wikipedia                #pip install wikipedia
import webbrowser #
import os #


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mayank")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Mayank")

    else:
        speak("Good Evening Mayank")

    speak("I am Bot Cubi. how may I help you")

if __name__=="__main__":
    wishMe()

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening.....")
        speak("I am Listening.....")
        r.pause_threshold = 1       #when we speak we take a gap pause threshold is used to gives us time to speak
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Can You Say that Again please....")
        return "None"
    return query

if __name__ == "__main__":
    # while True:
        query = takeCommand().lower()

         #logic foe executing tasks based on given query
        if 'wikipedia' in query:
            speak('searching Wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.register('chrome', None)
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query:
            webbrowser.register('chrome', None)
            webbrowser.open('https://www.google.com')

        elif 'open stack overflow' in query:

            webbrowser.register('chrome', None)
            webbrowser.open('https://www.stackoverflow.com')

        elif 'open google' in query:
            webbrowser.register('chrome', None)
            webbrowser.open('https://www.google.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(f"Mayank, The Time is {strTime}")

        elif 'open pictures' in query:
            picPath = "C:\\Users\\praja\\OneDrive\\Pictures"
            os.startfile(picPath)

        elif 'quit' in query:
            SystemExit



