from datetime import datetime
from email.mime import audio
from threading import main_thread
from unittest import result
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import*
from PyQt5.uic import loadUiType
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time


flags=QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
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
class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()

    def run(self):
        self.JARVIS()
    def STT(self):
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
     query=query.lower()
     return query
    def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('youremail@gmail.com','your-password')
     server.sednmail('youremail@gmail.com',to,content)
     server.close

    def JARVIS(self):
       wishme()
       while True:
        self.query=self.STT()

        if 'wikipedia' in self.query:
           speak('searching wikipedia.....')
           query = query.replace("wikipedia","")
           result = wikipedia.summary(query, sentences=2)
           speak("Accoding to Wikipedia")
           speak(result)
        elif 'open youtube' in self.query:
           webbrowser.open("youtube.com")
        elif 'open google' in self.query:
           webbrowser.open("google.com")
        elif 'open stackoverflow' in self.query:
           webbrowser.open("stackoverflow.com")
        elif'play music' in self.query:
           music_dir = 'D:\\New folder\\Audio'
           songs= os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in self.query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}") 
        elif 'open code' in self.query:
           codePath="D:\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
        elif 'turn off'in self.query :
           sys.exit()

       """elif 'email to harry' in query:
           try:
               speak("what should i say?")
               content= takeCommand()
               to="yourEmail@gmail.com"
               sendEmail(to,content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("sorry, i am not able to send email")"""
     


FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))
class Main(QMainWindow,FROM_MAIN):
    def __init__(self, parent=None): 
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7=QLabel
        
        Dspeak = mainT()
        self.label_7=QMovie("./gifloader.gif",QByteArray(),self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_6.setMovie(self.label_7)
        self.label_7.start()

        self.ts =time.strftime("%A,%d %B")
        Dspeak.start()
        self.label.setPixmap(QPixmap("./bg.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app= QtWidgets.QApplication(sys.argv)
main=Main()
main.show()
exit(app.exec_())

