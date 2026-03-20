def binConvert(n):
    return n // 2, n % 2

def findBinary(num):
    binary = ""

    while num > 0:
        quotient, remainder = binConvert(num)
        binary = str(remainder) + binary
        num = quotient
    
    return binary if binary else "0"

number = int(input("Enter number to convert to binary: "))

result = findBinary(number)
print(result)