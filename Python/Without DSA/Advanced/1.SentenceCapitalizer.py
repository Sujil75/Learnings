sentence = "build my own jarvis"

new_sentence = ""

for char in sentence.split(" "):
    first_letter = char[0].upper()

    new_char = first_letter + char[1:]

    new_sentence = new_sentence + " " + new_char

print(new_sentence)