num_list = list(map(int, input("Enter the number list with commas: ").split(",")))

missing_val = [x for x in range(1, num_list[-1]) if x not in num_list]


if len(missing_val) == 1:
    print(missing_val[0])
else:
    nums = ""
    for i in range(len(missing_val)):
        nums += str(missing_val[i]) + " "

    print(nums)


# 1,3,5,7,9,11,13,15