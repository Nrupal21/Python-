import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import openai
import datetime
import mysql.connector
import sys

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[1].id)

def Speak(audio):
    
    Assistant.say(audio)
    print(f"Jarvis: {audio}")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)
    
        try:
            print("Recognizing.....")
            query = command.recognize_google (audio, language='en-in')
            print (f"You Said: {query}")

        except Exception as error:
            return None

        return query


def Whatsapp():
    Speak("Tell Me The Name Of The Person!")
    name = takecommand() 
    
    if 'Aadarsh'or 'Adarsh' in name:
        Speak("Tell Me The Message!")
        msg = takecommand()
        Speak("Tell Me The Time Sir!")
        Speak("Time In Hour!")
        hour = int(input("Enter :"))
        Speak("Time In Minutes!")
        min = int(input(" Enter :"))
        pywhatkit.sendwhatmsg("+917972341450",msg,hour,min,10)
        Speak("OK Sir, Sending Whatsapp Message !") 

    
    elif 'Ayush Koli' in name:
        Speak("Tell Me The Message!")
        msg = takecommand()
        Speak("Tell Me The Time Sir!")
        Speak("Time In Hour!")
        hour = int(takecommand())
        Speak("Time In Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+919588493437 ",msg,hour,min,10)
        Speak("OK Sir, Sending Whatsapp Message !")
    
    elif 'unknown' in name:
        Speak ("What is The Number Of This Person" )
        phone=int(input("Enter Number Of This Person :"))  
        ph ='+91' + phone
        Speak("Tell Me The Message!")
        msg = takecommand()
        Speak("Tell Me The Time Sir!")
        Speak("Time In Hour!")
        hour = int(input("Enter"))
        Speak("Time In Minutes!")
        min = int(input("Enter"))
        pywhatkit.sendwhatmsg(ph,msg,hour,min,10)
        Speak("OK Sir, Sending Whatsapp Message !")


def OpenApps(b):
    Speak("Ok Sir, Wait A Second!")
    a=b

    if a==0: #code
        os.startfile("C:\\Users\\nrupal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
    elif a==1: #Epic Launcher' in query
        os.startfile("C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")
        
    elif a==2: #chrome in 
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    
    elif a==3: #'Photoshop' in query:
        os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe")

    elif a==4: #'facebook' in query:
        webbrowser.open('https://www.facebook.com/')

    elif a==5: #'insta' in query:
        webbrowser.open('https://www.instagram.com/')

    elif a==6: #Whatsapp 
        os.startfile('C:\\Users\\nrupal\\OneDrive\\Desktop\\WhatsApp.lnk')

    elif a==7: #youtube
        webbrowser.open('https://www.youtube.com/')



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=11:
        Speak("Good Morning!")
    elif hour>=12 and hour<=17:
        Speak("Good Afternoon!")
    else:
        Speak("Good evening!")
        
        
    Speak("I am jarvis sir please tell me how may  i help you")


def TaskExe():
    wishme()
    while True:
        query=takecommand()
        if 'YouTube search' in query:
            Speak("OK Sir, This Is What I found For Your Search!")
            query = query.replace("Jarvis", "")
            query = query.replace("YouTube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query 
            webbrowser.open(web)
            Speak("Done Sir")

        elif 'Google search' in query:
            Speak("OK Sir, This Is What I found For Your Search!")
            query = query.replace("Jarvis", "")
            query = query.replace("Google search", "") 
            pywhatkit.search(query)
            Speak("Done Sir")    
        
        elif 'website' in query:
            Speak("OK Sir, Launching....")
            query = query.replace("Jarvis", "")
            query = query.replace("website", "")
            web1 = query.replace("open","")
            web2 = 'https://www.'+web1+".com" 
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("OK Sir, Launching....")
        
        elif 'song' in query:
            Speak("OK Sir, This Is What I found For Your Search!")
            query = query.replace("Jarvis", "")
            query = query.replace("play", "")
            musicName = query.replace("song", "")
            pywhatkit.playonyt (musicName)
            Speak("Your Song Has Been Started!, Enjoy Sir!")

        elif 'Wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("Jarvis","")
            query = query.replace("Wikipedia","")
            wiki = wikipedia. summary(query,2)
            Speak (f"According To Wikipedia :{wiki}")  

        elif 'WhatsApp message' in query:
            Whatsapp()

        elif 'open code' in query:
            OpenApps(0)
        
        elif 'open Epic Launcher' in query:
            OpenApps(1)
        
        elif 'open Chrome' in query:
            OpenApps(2)
        
        elif 'open Photoshop' in query:
            OpenApps(3)
        
        elif 'open Facebook' in query:
            OpenApps(4)

        elif 'open Instagram' in query:
            OpenApps(5)

        elif 'open YouTube' in query:
            OpenApps(7)

        elif 'screenshot' in query:
            ss= pyautogui.screenshot()
            ss.save('D:\\Vs Code\\AI\\')

        elif 'hello' in query:
            Speak("Hello Sir, I Am Jarvis .") 
            Speak("Your Personal AI Assistant!") 
            Speak("How May I Help You?")

        elif '  ' in query:
            takecommand()

        elif 'how are you' in query: 
            Speak("I Am Fine Sir!") 
            Speak("Whats About YOU?")
        
        elif 'you need a break' in query:
            Speak ("Ok Sir, You Can Call Me Anytime !")
            break
        
        elif 'good bye' in query:
            Speak("Ok Sir, Bye")
            sys.exit()
