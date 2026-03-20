number = int(input("Enter number to check if armstrong: "))

length = len(str(number))

num_sum = sum(list(map(lambda x: int(x) ** length, str(number))))

result = number == num_sum

print(result)