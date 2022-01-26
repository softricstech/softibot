from msilib.schema import Error
import pyttsx3
import speech_recognition as sr

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print("   ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing......")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except Exception as Error:
            return "none"
            return query.lower()

query = takecommand()

if 'hello' in query:
    Speak("hello sir")

else: 
    Speak("no command found")