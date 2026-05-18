memory_file = "memory.txt"

def remember(text):
    with open(memory_file, "a") as f:
        f.write(text + "\n")
    return f"I will remember that: {text}"

def recall():
    try:
        with open(memory_file, "r") as f:
            data = f.readlines()
        return data[-1].strip()
    except:
        return "No memory found"

def search_memory(keyword):
    try:
        with open(memory_file, "r") as f:
            data = f.readlines()
        results = [line for line in data if keyword.lower() in line.lower()]
        return results[-1] if results else "Not found"
    except:
        return "Memory error"