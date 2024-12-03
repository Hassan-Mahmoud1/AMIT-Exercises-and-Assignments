import calc

while True:

    number = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    operation = input("Enter a command to perform: (add) (sub) (mul) (div): ").lower()

    if operation == 'add':
        print(f"The result is: {calc.add(number, number2)}")
    elif operation == 'sub':
        print(f"The result is: {calc.sub(number, number2)}")
    elif operation == 'mul':
        print(f"The result is: {calc.mul(number, number2)}")
    elif operation == 'div':
        print(f"The result is: {calc.div(number, number2)}")
    else:
        print("Error")
    another = input("Do you want to make another operation? yes, no, stop ").lower()
    if another =='stop' or another == 'no':
        print("Thanks for using the calculator!")
        break