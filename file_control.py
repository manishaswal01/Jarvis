import os

def create_file(name):
    with open(name, "w") as f:
        f.write("")
    return f"{name} created"

def open_file(name):
    os.startfile(name)
    return f"Opening {name}"

def delete_file(name):
    os.remove(name)
    return f"{name} deleted"