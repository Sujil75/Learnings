def getList(n):
    return set(filter(lambda x: n % x == 0, range(1, n)))

def findGCD(n1, n2):
    n1_list = getList(n1)
    n2_list = getList(n2)

    common_val_list = list(n1_list.intersection(n2_list))
    
    return max(common_val_list)
    

num1, num2 = map(int, input("Enter two numbers to find GCD with space between each numbers: ").split())

result = findGCD(num1, num2)
print(result)