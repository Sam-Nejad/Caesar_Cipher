# https://www.thecrazyprogrammer.com/2018/05/caesar-cipher-in-python.html

def encrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher


def decipher(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
    return cipher


def getOption():
    option = str(input("Do you want to encrypt, decipher or brute force a message?\n"))
    if option == "encrypt":
        text = input("Enter string to encrypt: ")
        if text.isalpha():
            shift = str(input("Enter shift number: "))
            if shift.isdigit():
                shift = int(shift)
                print("Original string: ", text)
                print("After encryption:", encrypt(text, shift) + "\n")
                runAgain()
            else:
                print("Given shift is not number.\n")
                getOption()
        else:
            print("Given string is not alphabetic.\n")
            getOption()
    if option == "decipher":
        text = input("Enter string to decipher: ")
        if text.isalpha():
            shift = str(input("Enter shift number: "))
            if shift.isdigit():
                shift = int(shift)
                print("Original string: ", text)
                print("After deciphering:", decipher(text, shift) + "\n")
                runAgain()
            else:
                print("Given shift is not number.\n")
                getOption()
        else:
            print("Given string is not alphabetic.\n")
            getOption()
    if option == "brute force":
        text = input("Enter string to brute force: ")
        if text.isalpha():
            print("Original string: ", text)
            alphabet = 26
            print("After deciphering:")
            for key in range(1, alphabet + 1):
                print(key, decipher(text, key))
            print("")
            runAgain()
        else:
            print("Given string is not alphabetic.\n")
            getOption()
    else:
        print("Not a valid choice, please choose either encrypt, decipher or brute force.\n")
        getOption()


def runAgain():
    option = input("Do you want to use this program again?\n")
    if option == "yes":
        getOption()
    elif option == "no":
        exit()
    else:
        print("Not a valid choice, please choose either yes or no.\n")
        runAgain()


getOption()
