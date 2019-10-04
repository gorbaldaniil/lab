def again():
    calc_again = input('''
    Do you want to calculate again?
    Type Y for YES, or N for NO. 
    ''')
    if calc_again == 'Y':
        calc()
    elif calc_again == 'N':
        print('See you later.')
    else:
        again()


def calc():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    operation = input("""
    For addition enter +
    For subtraction enter -
    For multiplication enter *
    For division enter /
    """)

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    print("Результат = ", result)
    again()

calc()

