print("This is to find the number of words repeated in a given sentence, result will be shown in lower case in spite of what case are used")
user_input = input("Enter a sentence: ").split(" ")

freq = {}
for word in user_input:
    word = word.lower()

    freq[word] = freq.get(word, 0) + 1

print(freq)