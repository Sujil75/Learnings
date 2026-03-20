number = int(input("Enter a number to get its multiplication values: "))

multiple_range = range(1, 11)
multiplication_list = list(map(lambda x: x * number, multiple_range))

print(multiplication_list)