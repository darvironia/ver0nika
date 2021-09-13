import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
    print(words)
    os.system("say " + words)

talk("Hello, ask me about something")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk("Say what you want")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_sphinx(audio).lower()
        print(task)
    except sr.UnknownValueError:
        talk("I didn't understand you")
        task = command()
    
    return task

def makeSomething(task):
    if 'open website' in task:
        talk("Opening website")
        url = 'https://itproger.com'
        webbrowser.open(url)
    elif 'stop' in task:
        talk("Yes, of course, no problem")
        sys.exit()

while True:
   makeSomething(command())