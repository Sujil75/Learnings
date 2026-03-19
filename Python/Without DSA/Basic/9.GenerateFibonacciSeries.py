def findFibonacci(num):
    series = []
    a, b = 0, 1

    for _ in range(num):
        series.append(a)

        a, b = b, a + b
    
    return series

number = int(input("Enter the number to find Fibonacci series: "))

result = findFibonacci(number)
print(result)