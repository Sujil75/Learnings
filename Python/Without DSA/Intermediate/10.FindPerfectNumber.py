def findSum(n):
    return sum(list(filter(lambda x: n % x == 0, range(1, n))))

def checkPerfectNum(num):
    num_sum = findSum(num)

    return num_sum == num

number = int(input("Enter a number to check if perfect number: "))

result = checkPerfectNum(number)
print(result)