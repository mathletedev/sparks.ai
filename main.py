import speech_recognition as sr
import pyttsx3
import subprocess

USERNAME = "Neal"
BOT = "sparks"

engine = pyttsx3.init()

engine.setProperty("rate", 180)
engine.setProperty("voice", "english+f2")


def say(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone(device_index=5) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-CN")
    except:
        say("I didn't quite get that, could you please say that again?")
        query = None

    return query


def main():
    while True:
        query = listen()
        print(query)
        if query is None:
            continue
        query = query.lower()

        if query == "hello":
            say("Hello Neal, how may I help you?")

        if "open" in query:
            if "terminal" in query:
                subprocess.Popen("kitty")
                say("Opened new terminal instance")

            if "brave" in query or "browser" in query:
                subprocess.Popen("brave")
                say("Opened new Brave instance")


if __name__ == "__main__":
    main()
