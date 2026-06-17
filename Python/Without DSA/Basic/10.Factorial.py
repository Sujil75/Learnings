def findFactorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i
    
    return fact

number = int(input("Enter the number to find its factorial: "))

result = findFactorial(number)
print(result)