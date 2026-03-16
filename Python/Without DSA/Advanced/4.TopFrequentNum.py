# check: 12233344445

numbers = list(map(int, input("Enter numbers: ")))

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

max_value = max(freq, key=freq.get)

print(max_value)