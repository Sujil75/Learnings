print("Palindrome are the words which in reversing gives the output same as the input. Eg. madam")
user_input = input("Enter a word to check palindrome: ")

word = user_input.lower()

if word == word[::-1]:
    print(True)
else:
    print(False)