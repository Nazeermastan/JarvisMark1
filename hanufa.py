import pyttsx3
import speech_recognition as sr
import datetime #built in function
import wikipedia
import webbrowser #built in function
import os #built in function
import smtplib #built in function
import pywhatkit as kit
import subprocess as sp #built in function

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello Nazeer.....Very Good Morning")

    elif hour>=12 and hour<18:
        speak("Hello Nazeer....Good Afternoon")

    else:
        speak("Good Evening!")

    speak(" CHITTI ROBO is here to help you.")
    print('__________________________________________________________________________________________________________________________________________')
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening........")
        r.pause_threshold=0.5
        audio = r.listen(source)
    try:
        print(" ")
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        print(e)    
    return query

def play_on_youtube(video):
    kit.playonyt(video)
    exit()

def get_from_chatgpt(order):
  kit.playonchatgpt(order)
  exit()


def camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    exit()

def search_on_google(query):
    kit.search(query)
    exit()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nazeerbro7@gmail.com','799*****77')
    server.sendmail('nazeermastan4@gmail.com', to, content)
    server.close()

if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = takeCommand().lower()
            play_on_youtube(video)

        elif 'open camera' in query:
            camera()

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'google' in query:
            speak('What do you want to search on Google, sir?')
            query = takeCommand().lower()
            search_on_google(query)

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'music' in query:
            music_dir = "C:\\Users\\Nazeer Mastan\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            speak('enjoy the music boss!')
            os.startfile(os.path.join(music_dir, songs[2]))
            exit()

        elif 'Ordering' in query:
            speak('Give command Sir!')
            order = takeCommand().lower()
            

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Boss, the time is {strTime}")

        elif 'open netflix' in query:
            speak("Let's watch the Peaky blinders on netflix boss")
            webbrowser.open("www.netflix.com")

        elif 'open prime' in query:
            speak('Opening the prime Boss')
            webbrowser.open('www.amazonprime.com')

        elif 'open disney hotstar' in query:
            speak('Initiating the hotstar Boss')
            webbrowser.open('www.hotstar.com')

        elif 'how are you' in query:
            speak('I am fine Nazeer, how about you?')

        elif 'send mail' in query:
            try:
                speak('what is the content?')
                content=takeCommand()
                to = 'nazeermastan4@gmail.com'
                sendEmail(to, content)
                speak('Email sent!')
            except Exception as e:
                print(e)
                speak('Ooops cannot send the mail')

        elif 'quit' in query:
            speak('Quitting Boss')
            exit()
