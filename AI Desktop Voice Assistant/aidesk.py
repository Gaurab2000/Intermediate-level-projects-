from datetime import datetime
from email.mime import audio
from threading import main_thread
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
        hour=int (datetime.datetime.now().hour)
        if hour>=0 and hour <12:
            speak("Good Morning Gaurrab!")
        elif hour>=12 and hour<=18:
            speak("Good Afternoon Gaurrab!")
        else:
            speak("Good Evening Gaurrab!")
        
        speak("Jarvis at your service, how may i help you ?")
def takeCommand():
  #it takes microphone input from the user and return string output
    r= sr.Recognizer()
    with sr.Microphone()as source:
        print("I am listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
         print("Recognizing...")    
         query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
         print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sednmail('youremail@gmail.com',to,content)
    server.close

if __name__=="__main__":
  wishme()
  while True:
       query=takeCommand().lower()

       if 'wikipedia' in query:
           speak('searching wikipedia.....')
           query = query.replace("wikipedia","")
           result = wikipedia.summary(query, sentences=2)
           speak("Accoding to Wikipedia")
           speak(result)
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           webbrowser.open("google.com")
       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")
       elif'play music' in query:
           music_dir = 'D:\\New folder\\Audio'
           songs= os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
       elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}") 
       elif 'open code' in query:
           codePath="D:\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
       elif 'email to harry' in query:
           try:
               speak("what should i say?")
               content= takeCommand()
               to="yourEmail@gmail.com"
               sendEmail(to,content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("sorry, i am not able to send email")
       elif 'turn off'in query :
           break  
