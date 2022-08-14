import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyautogui
import pyjokes
import screen_brightness_control as sbc
import os
import time
import subprocess
import wolframalpha
import json
import requests
import brightness
from wifi import wifi
import volume


print('Loading your AI personal assistant')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():

    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")

    elif hour  >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")


        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your AI personal assistant")

wish_me()

if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = take_command().lower()

        if statement == 0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant is shutting down,Good bye')
            print('your personal assistant is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(3)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(3)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = take_command()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,'
                  'google chrome,'
                  'gmail and '
                  'stackoverflow ,'
                  'predict time,'
                  'search wikipedia,'
                  'predict weather in different cities,'
                  'get top headline news from times of india '
                  'and you can ask me computational or geographical questions too!,'
                  'I can also do System Operation like increase volume, brightness ,shutting down connecting to wifi etc')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by prathi, kitchu and muhil")
            print("I was built by prathi, kitchu and muhil")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = take_command()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            # pywhatkit.playonyt(song)

        elif 'joke' in statement:
            speak(pyjokes.get_joke())

        elif 'find location' in statement:

            location = statement.replace('location', "")
            url = 'https://google.nl/maps/place/' + location + '/$amp;'
            webbrowser.get().open(url)
            speak('Here is the location of' + location)

        elif 'volume up' in statement:
            volume.volume_up()
            speak('volume increased')
        elif 'volume down' in statement:
            volume.volume_down()
            speak('volume decreased')
        elif 'volume mute' in statement:
            volume.volume_mute()
            speak('volume muted')
        elif 'full brightness' in statement:
            brightness.increase_brightness()
            speak('Device is in full brightness')
        elif 'zero brightness' in statement:
            brightness.zero_brightness()
            speak('Device is in zero brightness')
        elif 'increase brightness' in statement:
            brightness.increase_brightness()
            speak('Device brightness is increased by 25%')
        elif 'decrease brightness' in statement:
            brightness.decrease_brightness()
            speak('Device brightness is decreased by 25%')
        elif 'half brightness' in statement:
            brightness.half_brightness()
            speak('Device is in half brightness')

        elif "connect wi" in statement:
            wifi()

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])



time.sleep(3)
