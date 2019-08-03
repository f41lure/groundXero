import speech_recognition as sr  
import os
import subprocess
import time
 
# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)
    listening = True

list1 = []
print("Listening and processing")
while listening == True:
    for i in range(3):
        print('.', end='')
        list1.append('.')
        time.sleep(1)
        if len(list1) == 3:
            print('\b\b\b')
            del list1[:]
    try:
        listening = False
        print("OK", r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))




##subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application'])
## Add paths to whatever programs you want

if r.recognize_google(audio) == "google" or r.recognize_google(audio) == "Google":
    os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome')

elif r.recognize_google(audio) == "IE" or r.recognize_google(audio) == "explore" or r.recognize_google(audio) == "Internet Explorer" or r.recognize_google(audio) == "internet explorer":
    os.startfile('C:\Program Files (x86)\Internet Explorer\iexplore')

elif r.recognize_google(audio) == "File Explorer":
    os.startfile('C:')

elif r.recognize_google(audio) == "Firefox" or r.recognize_google(audio) == "Fire fox" or r.recognize_google(audio) == "fire":
    os.startfile('C:\Program Files\Mozilla Firefox')
