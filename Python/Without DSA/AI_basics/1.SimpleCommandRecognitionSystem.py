user_input = input("Enter a command: ").split(" ")

commands = ["remember", "search", "open", "command"]

recognizer = {}
data = []
for word in user_input:
    if word.lower() in commands:
        recognizer["command"] = word
    else:
        data.append(word)
        recognizer["data"] = recognizer.get("data", data)

print(recognizer)