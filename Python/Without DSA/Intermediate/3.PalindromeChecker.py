def check_palindrome():
    string = input("Enter value to check if palindrome: ")

    new_string = ""

    for char in string:
        new_string = char + new_string

    print()
    if string.lower() == new_string.lower():
        print(True)
    else:
        print(False)

    print('\n')
    do_again = input("Do again Y/N: ")

    match do_again:
        case "y" | "Y":
            check_palindrome()
        case "n" | "N":
            exit()


check_palindrome()