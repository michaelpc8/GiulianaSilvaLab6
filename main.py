#Giuliana Silva
#TEST
#encode function
def encode(numbers):
    newNumber = ""
    if len(numbers) == 8:
        for digit in numbers:
            newDigit = int(digit) + 3

            if newDigit > 9:
                newDigit = str(newDigit)
                listdigit = list(newDigit)
                newDigit = listdigit[1]

            newNumber += str(newDigit)

        return newNumber
#Michael Pierre-Canel
def decode(newNumbers):
    if len(newNumbers) == 8:
        for digit in newNumbers:
            newDigit = int(digit) - 3

            if newDigit > 9:
                newDigit = str(newDigit)
                listdigit = list(newDigit)
                newDigit = listdigit[1]

            newNumbers += str(newDigit)

        return newNumbers
        
#main logic
if __name__ == '__main__':
    condition = True



    while condition == True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_input =input("Please enter and option: ")

#takes user input to produce an output
        if user_input == "1":
            numbers = input("Please enter your password to encode: ")
            encNum = encode(numbers)
            print("Your password has been encoded and stored!")

        if user_input == "2":
            print(f"The encoded password is {encNum}, and the original password is {numbers}.")

        if user_input == "3":
            condition = False
