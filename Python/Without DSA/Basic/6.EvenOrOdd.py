print("To check a number is even or odd")


def checkOddOrEven(num):
    return "Even" if num % 2 == 0 else "Odd"
    

def doAgain():
    userInput = input("Do again? Y/n: ")

    match userInput:
        case 'Y' | 'y':
            print()
            getInput()
        case 'N' | 'n':
            print('Ok, Thank you')
            exit()
        case _:
            print('Invalid Input, try again \n')
            doAgain()

def getInput():
    number = int(input("Enter a number: "))

    result = checkOddOrEven(number)
    print('Result: ', result, '\n')
    
    doAgain()

getInput()