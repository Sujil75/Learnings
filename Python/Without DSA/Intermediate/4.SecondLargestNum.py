def findSecondLargestVal():
    array = list(input("Enter numbers: "))
    array = list(set(filter(lambda x: x != " ", array)))

    second_largest = sorted(array)[-2]

    print(second_largest)

findSecondLargestVal()