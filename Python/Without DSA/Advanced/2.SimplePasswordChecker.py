def checkPassword(p):
    if len(p) < 8:
        return "Weak password, increase the length to be minimum of 8 chars"
    
    has_num = any(each.isdigit() for each in p)

    if not has_num:
        return "Weak password, add a number"
    
    has_upper = any(each.isupper() for each in p)

    if not has_upper:
        return "Weak password, add upper case char"
    
    return "Strong Password"

def getPassword():
    password = input("Enter password: ")

    result = checkPassword(password)

    return result

def retry():
    def tryAgain(result):
        match result:
            case 'Y' | 'y':
                print('\n')
                doAgain()
            case 'N' | 'n':
                print('Thank you \n')
                exit()
            case _:
                print("Didn't get a valid answer, try again")
                print()
                retry()

    do_again = input("Want to try again? Y/n: ")

    tryAgain(do_again)


def doAgain():
    verified = getPassword()

    print(verified)

    print('\n')

    retry()

doAgain()