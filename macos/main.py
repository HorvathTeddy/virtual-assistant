from re import search
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui
import os
import subprocess 
import sys
from bs4 import BeautifulSoup
from keyboard import press
from keyboard import press_and_release
import webbrowser
import requests

listener = sr.Recognizer()
engine = pyttsx3.init('nsss')
rate = engine.getProperty("rate")
engine.setProperty("rate", 250)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    

talk('Hello sir')

def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        global command
        command = listener.recognize_google(voice)
        command = command.lower()
    return command
    
def run_computer():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        if 'pause' in command:
            press('pause')       

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('it is ' + time)
        
    elif 'wikipedia' in command:
        wiki = command.replace('wikipedia', '')
        info = wikipedia.summary(wiki, 1)
        print(info)
        talk(info)
                
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'volume up 4' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 6' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 8' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 10' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 12' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 14' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 16' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 18' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 20' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 30' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 40' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume down 4' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 6' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 8' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 10' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 12' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 14' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 16' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 18' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 20' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 30' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 40' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedowm")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume mute' in command:
        pyautogui.press("volumemute")

    elif 'league of legends' in command and 'computer' in command:
        subprocess.call(r'[pathname]')  # enter pathname without brackets 

    elif 'spotify' in command and 'computer' in command:
        subprocess.call(r"[pathname]")  # enter pathname without brackets 

    elif 'discord' in command:
        subprocess.call(r"[pathname]")  # enter pathname without brackets 

    elif 'shut down' in command or 'power off' in command:
        sys.exit()

    elif 'temperature' in command or 'weather' in command:
        search = "local temperature"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        talk(f"it is {temp}")
    
    elif 'search' in command:
        search = command.replace('search', '')
        pywhatkit.search(search)

    # elif 'screenshot' in command:
    #     talk('What shall I name the image sir?')
    #     path = take_command()
    #     path1name = path + ".png"
    #     path1 = "&&\\Users\\Teddy Horvath\\Pictures\\screenshots\\" + path1name
    #     ss = pyautogui.screenshot()
    #     ss.save(path1)
    #     os.startfile("[pathname]") # enter pathname without brackets 

    else:
        print('please repeat that sir')

    while True:
        run_computer()

run_computer()