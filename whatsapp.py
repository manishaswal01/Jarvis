import pywhatkit

def send_message(number, message):
    pywhatkit.sendwhatmsg_instantly(number, message)
    return "Message sent"