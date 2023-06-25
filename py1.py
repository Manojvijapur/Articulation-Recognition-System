# import pyttsx3


# engine = pyttsx3.init('sapi5')
# voices = engine.getproperty('voices')
# print(voices)
# print(voice[0].id)
# engine.setProperty('voice' , voice[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# 
# import pyttsx3

# engine = pyttsx3.init()

# voices= engine.getProperty('voices') #getting details of current voice

# engine.setProperty('voice', voices[0].id)
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
# engine.say("Hello Manoj!")
# engine.runAndWait()
voices= engine.getProperty('voices')
print(len(voices))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    password = 'hello'
    speak("Enter the password to access the voice assistant:")
    while True:
        user_password=takeCommand().lower()
        if user_password == password:
            speak("Access granted!")
            break
        else:
            speak("Access denied! Please try again.")

    # Rest of the function code
    # ...

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:

        speak("Good Afternoon!")

    elif hour>=18 and hour<20:

        speak("Good Evening!")

    else:

        speak("Good Night!")

    speak("Hey MANOJ! I'm a personal voice assistant. What you want to do? ")

def takeCommand():

    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        print("Speak to the assistant loudly...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")  #Say that again will be printed in case of improper voice
        return "None" #None string will be returned
    return query

if __name__== "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'play music' in query:
            # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            # songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir, songs[0]))
            engine.say("First things first I'ma say all the words inside my head I'm fired up and tired of the way that things have been, oh-oohThe way that things have been, oh-ooh")
            engine.runAndWait()
        elif 'stop' in query:
            engine.stop()

        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'about venkat' in query:
            str = ("The guy with a sarcastic brain and a very kind human being")
            speak(f"The guy with a sarcastic brain and a very kind human being {str}")

        elif 'about akshay' in query:
            str = ("The guy who is very much friendly and caring one and my best friend forever")
            speak(f"The guy who is very much friendly and caring one and my best friend forever {str}")

        elif 'about narayan' in query:
            str = ("The guy who works in TCS currently and a very good friend")
            speak(f"The guy who works in TCS currently and a very good friend {str}")

        elif 'about me' in query:
            str = ("The guy who loves sports and music to the core and an orthodox person")
            speak(f"The guy who loves sports and music to the core and a fun loving person {str}")

        elif 'about our guide' in query:
            str = ("DR. R H GOUDAR Dept of Computer Science and Engineering, Visvesvaraya Technological University, Jnana Sangama Belagavi, Karnataka, India. Designation: Associate Professor Department of Computer Science and Engineering Visvesvaraya Technological University")
            speak(f"DR. R H GOUDAR Dept of Computer Science and Engineering, Visvesvaraya Technological University, Jnana Sangama Belagavi, Karnataka, India. Designation: Associate Professor Department of Computer Science and Engineering Visvesvaraya Technological University {str}")
        else:
            str = ("Result not found")
            speak(f"Result not found {str}")
            print(str)

        # elif 'open code' in query:
        #     codePath = "/home/user/Desktop/Doremon/py1.py"
        #     os.startfile(codePath)

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()


    takeCommand()

