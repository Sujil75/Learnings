def checkPrime(nums):
    if nums <= 1: return False

    if nums == 2: return True

    if nums % 2 == 0: return False

    for num in range(3, nums // 2 + 1, 2):
        if nums % num == 0:
            return False
    
    return True

number = int(input("Enter a value to check for prime: "))

result = checkPrime(number)

print(result)