import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os
import re
import random
import sys
import requests
import smtplib

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('3AL5K8-8K52GRGRGE')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("wait!")
engine.say("3")
engine.say("2")
engine.say("1")
engine.say("JARVIS is ready to set fire")



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("say that again please")
        print("say that again please..")
        query = str(input('command:'))
        
    return query

def userName():
    speak("what's the username")
    user= input("enter the username")
    
    if user == "devesh":
        speak("ok! thank you")
    else:
        speak("username is not correct")
        print("Username is not correct")
        sys.exit()
             

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("ok!, good morning! Devesh")

    elif hour>=12 and hour<18:
        speak("ok!,good afternoon! Devesh")

    else:
        speak("ok!,good evening! Devesh")
    speak("I am Jarvis sir. please tell me how may help you")



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your E-Mail', 'your Password')
    server.sendmail('your email', to, content)
    server.close()


if __name__ == "__main__":
        userName()
        wishMe()
        while True:
            query = takeCommand().lower()
        
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(result)
                speak(result)

            elif 'open youtube' in query:
                 url ="youtube.com"
                 chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                 webbrowser.get(chrome_path).open(url)

            elif 'open google' in query:
                 url ="google.com"
                 chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                 webbrowser.get(chrome_path).open(url)
            
            elif 'open my gmail' in query:
                 url = "mail.google.com"
                 chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                 webbrowser.get(chrome_path).open(url)

            elif 'play music' in query:
                 music_dir = 'E:\\song'
                 songs = os.listdir(music_dir)
                 print(songs)    
                 os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                 strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                 print(strTime)   
                 speak(f"Sir, the time is {strTime}")

            elif 'nothing' in query or 'abort' in query or 'stop' in query:
                 speak("Bye Sir, have a good day.")
                 sys.exit()
                    
            
            elif 'hello' in query:
                 speak('Hello Sir')
        

            elif 'open website' in query or 'go to' in query:
                    reg_ex = re.search('open website (.+)', query)
                    if reg_ex:
                        domain = reg_ex.group(1)
                        url = 'https://www.' + domain
                       # webbrowser.open(url)
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open(url)
                        speak('Done!')
                    else:
                        pass
            
            elif 'send email' in query:
                speak("who is the recipient")
                recipient = takeCommand()
                if 'david' in recipient:

                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "recipient mail id"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry my friend. I am not able to send this email")  
                        
                elif 'sara' in recipient:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "recipient mail id"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry my friend. I am not able to send this email")

                elif 'mam' in recipient:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "recipient mail id"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry my friend. I am not able to send this email")  
                
                else:
                    speak("sorry sir i can't find recipient")



            else:
                query = query
                speak("searching...")
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak("got it")
                        print(results)
                        speak(results)
                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak("got it")
                        
                        print(results)
                        speak(results)
                except:
                    url='www.google.com'
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    webbrowser.get(chrome_path).open(url)
            speak("ok!, any other command for me sir...")


   