def forConversion(n, i):
    val = int(n[-i - 1])
    power = 2 ** i

    return val * power

def convertBinaryToDecimal(num):
    decimal = 0
    length = len(num)
    
    for i in range(length - 1, -1, -1):
        val = forConversion(num, i)
        decimal += val

    return decimal
        


number = input("Enter the binary to decimal: ")

result = convertBinaryToDecimal(number)
print(result)