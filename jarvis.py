import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import random
import cv2
import pyautogui
import time
import operator
import requests
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("What can i do for you ?")

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            print("Yes sir")
            speak("Yes sir")
        elif "who are you" in query:
            print("My name is Jarvis")
            speak("My name is Jarvis")
            print("I can do Everything that my creator programmed me to do")
            speak("I can do Everything that my creator programmed me to do")
        elif "who created you" in query:
            print("Chetan don")
            speak("Chetan don")
        elif "what is" in query:
            speak("Searching Wikipedia...")
            query = query.replace("what is", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            print(results)
        elif 'just open google' in query: 
            webbrowser.open("https://www.google.com")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
        elif 'open google' in query: 
            speak("what should I search ?")
            qry = takeCommand().lower() 
            webbrowser.open(f" (qry)")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)
        elif 'just open youtube' in query: 
            webbrowser.open("youtube.com")

        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")

        elif 'search on youtube' in query: 
            query= query.replace("search on youtube", "") 
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif "open chrome" in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)
        elif 'close browser' in query:
            os.system("taskkill /f /im msedge.exe")
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        # elif "search on chrome" in query:
        #     try:
        #         speak("What should I search?")
        #         print("What should I search?")
        #         chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        #         search = takeCommand()
        #         webbrowser.get(chromePath).open_new_tab(search)
        #         print(search)

        #     except Exception as e:
        #         speak("Can't open now, please try again later.")
        #         print("Can't open now, please try again later.")
            
        # elif "open paint" in query:
        #     npath=""
        #     os.startfile("npath")
        # elif "close paint" in query:
        #     os.system("")
        # elif "open notepad" in query:
        #     npath=""
        #     os.startfile("npath")
        # elif "close notepad" in query:
        #     os.system("")
        # elif "open command prompt" in query:
        #     os.system("start cmd")
        # elif "close command prompt" in query:
        #     os.system("")
        elif 'open camera' in query: #28
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50) 
                if k==27:
                    break; 
            cap.release()
            cv2.destroyAllWindows()
        elif "go to sleep" in query: #29
            speak("alright then, I am switching off")
            sys.exit()
        elif "take screenshot" in query: #30
            speak("tell me a name for the file")
            name =takeCommand().lower()
            time.sleep(3)
            img= pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")
        elif "calculate" in query: #31
            r=sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listning...")
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source) 
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+':operator.add,
                    '-':operator.sub,
                    'x':operator.mul,
                    "divided" : operator.__truediv__,
                }[op]
            def eval_bianary_expr(op1,oper, op2):
                op1, op2 = int(op1), int (op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr((my_string.split())))

        elif "what is my IP address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
        elif "offline" in query:
            quit()

        



        
            

        