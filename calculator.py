while True:

    print("1. Enter a first number")
    print("2. Enter an operator")
    print("3. Enter a second number")
    print("4. Exit")

    choose = int(input("Choose the value: "))

    match choose:

        case 1:
            x1 = int(input("Enter first number: "))

        case 2:
            operator = input("Enter operator (+,-,/,*): ")

        case 3:
            x2 = int(input("Enter second number: "))

        case 4:
            print("Exit")
            break

        case _:
            print("Invalid choice")


if 'x1' in locals() and 'operator' in locals() and 'x2' in locals():

    if operator == '+':
        print("Answer =", x1 + x2)

    elif operator == '-':
        print("Answer =", x1 - x2)

    elif operator == '*':
        print("Answer =", x1 * x2)

    elif operator == '/':
        if x2 != 0:
            print("Answer =", x1 / x2)
        else:
            print("Cannot divide by Zero")

    else:
        print("Invalid operator")