string = input("Enter a string: ")

vowels = "aeiou"
# count = 0

# for char in string:
#     if char in vowels:
#         count += 1

count = len(list(filter(lambda x: x in vowels, string)))

print(count)        