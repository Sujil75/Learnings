number = int(input("Enter the number to find its divisors: "))

result = list(filter(lambda num: number % num == 0, range(1, number + 1)))

print(result)