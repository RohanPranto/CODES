import speech_recognition as sr
import pyttsx3
import pywhatkit 

listener = sr.Recognizer()
engine = pyttsx3.init()
# to set to female voice, uncommand next two lines
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def talk(text):
    # engine.say('whats up human, how can i help you')
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'kaju' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

run_alexa()