import eel
import pyttsx3
from commands import handle_commands
from ai import get_ai_response

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    eel.displayMessage(text)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def allCommands(message):
    query = message.lower()

    cmd = handle_commands(query)

    if cmd:
        speak(cmd)
    else:
        ai = get_ai_response(query)
        speak(ai)

eel.init("web")
eel.start("index.html", size=(1000, 800))