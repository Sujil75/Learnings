print("Enter numbers without space comma or anything to find the sum of the numbers, Eg: 12345")

def addingNums(nums):
    adding = 0

    for num in nums:
        adding += num

    return adding

def doAgain():
    userInput = input('Want to try again? Y/n: ')

    match userInput:
        case 'Y' | 'y':
            print()
            getInput()
        case 'N' | 'n':
            print('Ok, Thank you')
            exit()
        case _:
            print('Invalid input, try again \n')
            doAgain()


def getInput():
    num_list = list(map(int, input('Enter the list: ')))

    result = addingNums(num_list)
    print('Result:', result, '\n')

    doAgain()

getInput()