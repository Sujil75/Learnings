def pyramidPattern(s):
    num = ""

    for i in range(1, s + 1):
        num += str(i)
        print(num)    

steps = int(input("Enter the number of steps: "))

pyramidPattern(steps)