from datetime import datetime
import webbrowser
import os
from memory import *
from search import *
from file_control import *
from whatsapp import *
from automation import *

def handle_commands(query):
    query = query.lower()

    if "time" in query:
        return datetime.now().strftime("%I:%M %p")

    elif "open chrome" in query:
        os.system("start chrome")
        return "Opening Chrome"

    elif "search" in query:
        q = query.replace("search", "")
        return google_search(q)

    elif "remember" in query:
        return remember(query.replace("remember", ""))

    elif "what did i say" in query:
        return recall()

    elif "create file" in query:
        return create_file("test.txt")

    elif "delete file" in query:
        return delete_file("test.txt")

    elif "whatsapp" in query:
        return send_message("+91XXXXXXXXXX", "Hello from Jarvis")
    
    elif "screenshot" in query:
        return take_screenshot()

    elif "volume up" in query:
        return volume_up()

    elif "volume down" in query:
        return volume_down()

    elif "reminder" in query:
        return set_reminder(10, "This is your reminder")

    return None