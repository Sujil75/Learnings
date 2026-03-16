string = "mississippi"

# Method 1

freq = {}

for char in string:
    freq[char] = freq.get(char, 0) + 1

print(freq)


# Method 2

# freq = {char: string.count(char) for char in set(string)}

# freq = sorted(freq.items())

# print(freq)