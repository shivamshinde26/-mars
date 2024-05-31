from ast import Try
from logging import exception
from pickle import TRUE
from threading import main_thread
from pip import main
import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir ")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
          print("Say something!")
          print('Listening...')
          r.pause_threshold=0.5
          audio=r.listen(source)  
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("You Said: ",query) 
    except Exception as e:
        speak("I think i missed something")
        return "None"
    return query
if __name__=="__main__":
  wishMe()
  speak(" How May I Help You ?")
  while True:
      query=takeCommand().lower()
      if 'wikipedia' in query:
          speak("Just A Second")
          query=query.replace('wikipedia', '')
          results=wikipedia.summary(query,sentences=2)
          speak("According To Wikipedia")
          speak(results)
          print(results)
      elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("opening youtube")
      elif 'check my pending assignments on google classroom' in query:
          webbrowser.open("https://classroom.google.com/a/not-turned-in/all")
          speak("opening google classroom")           
      elif 'open google' in query:
          webbrowser.open("https://www.google.com/")
          speak("opening google")
      elif 'food' in query:
          webbrowser.open("https://www.zomato.com/")
          speak("Opening Zomato")  
      elif 'what is the cricket score' in query:  
          webbrowser.open("https://www.cricbuzz.com/")
          speak("opening crickbuzz") 
      elif 'messages on instagram' in query:
          webbrowser.open("https://www.instagram.com/direct/inbox/")
          speak("opening instagram")
      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")    
          speak(f"the time is {strTime}")
      elif 'weather' in query:
          webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1OKWM_enIN915IN915&oq=weather&aqs=chrome..69i57j35i39j0i67l2j0i67i433i457j0i402l2j69i61.2597j0j7&sourceid=chrome&ie=UTF-8")
          speak("checking weather in vishrambhag,sangli") 
      elif ' your favourite actor' in query:
          speak("There are lot great actors but shahrukh khan is my favourite actor!!") 
      elif ' your favourite cricketer' in query:
          speak("the god of cricket 'sachin tendulkar'  ") 
      elif ' your favourite ipl team' in query:
          speak("the mighty MUMBAI indians is my favourite ")     
      elif ' your favourite cricketer' in query:
          speak("the one and only sachin tendulkar ") 
      elif 'the time' in query:
          strTime= datetime.datetime.now().strftime("%H:%M")       
          speak("the current time is",strTime)
      elif 'joke'  in query:
          speak(pyjokes.get_jokes())
          speak('hahaha')     
      elif  'play' in query:
          song=query.replace('play','')
          speak('playing'+ song)
          pywhatkit.playonyt(song) 
      elif 'name' in query:
          speak("my name is Mars")  
          print(speak) 
      elif 'how are you' in query:
        speak("i am fine sir!")
      elif 'what are you doing' in query:
          speak("nothing just doing my assigned work")
      elif 'tell me about' in query:
          web=query.replace('tell me about','')
          speak("showing results for "+ web)
          pywhatkit.search(web)
      elif 'are donkey' in query:
          speak("Come on everyone is not like you ")     
      elif 'you married' in query:
          speak("yes i am married to your wifi")
      elif 'do nothing' in query:
          speak("call me if you need it")
          break
      elif 'wait' in query:
          speak("thank you sir for calling me, and if you need it again, MARS will be there, have a wonderful day")
          break
      else:
          speak("I don't know what are you talking about speak clearly my friend")