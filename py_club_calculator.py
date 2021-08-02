import time


# Calculator
# welcome message and asking for the operation to perform
def welcome():
    list_of_operation = ['addition', 'subtraction', 'division', 'multiply']
    print('Hello User\n')
    print(f'Operation you can perform => {list_of_operation}')
    time.sleep(1)
    users_request = input('Please what operation do you want to perform:\n:>')
    time.sleep(2)
    print(f'Okay {users_request}')
    print()
    if users_request == 'addition' in list_of_operation:
        addition()
    if users_request == 'subtraction' in list_of_operation:
        subtraction()
    if users_request == 'division' in list_of_operation:
        division()
    if users_request == 'multiply' in list_of_operation:
        multiply()
    while True:
        if users_request not in list_of_operation:
            print('Not found in operation type again...')
            continuing()


def continuing():
    list_of_operation = ['addition', 'subtraction', 'division', 'multiply']
    print(f'Operation you can perform => {list_of_operation}')
    time.sleep(1.5)
    users_request = input('Please what operation do you want to perform:\n:>')
    time.sleep(1)
    print(f'Okay {users_request}')
    print()
    if users_request == 'addition' in list_of_operation:
        addition()
    if users_request == 'subtraction' in list_of_operation:
        subtraction()
    if users_request == 'division' in list_of_operation:
        division()
    if users_request == 'multiply' in list_of_operation:
        multiply()
    while True:
        if users_request not in list_of_operation:
            print('Not found in operation type again...')
            continuing()


def requesting_continuing():
    while True:
        u_input = input('Do you want to continue: yes/no\n =>')
        if u_input == 'yes':
            continuing()
        if u_input == 'no':
            exit()


# function for addition
def addition():
    print('Hit 0 to show answer')
    # appending users input to add
    list_add = []
    try:
        # taking users input
        while True:
            # taking inputs in floats
            users_add = float(input('argument:'))
            if users_add == 0:
                print(f'=> The answer is: {sum(list_add)}')
                break
            else:
                list_add.append(users_add)
        # asking the user if wants to continue with another operation
        requesting_continuing()
    except ValueError:
        print('Type a number')
        #  restart if a value error
        addition()


def subtraction():
    while True:
        try:
            user_input = float(input('argument: '))
            user_input2 = float(input('argument: '))
            answer = user_input - user_input2
            print(f'=> {answer}')
            # asking the user if wants to continue with another operation
            requesting_continuing()
        except ValueError:
            print('Type a number')
            #  restart if a value error
            subtraction()


def division():
    while True:
        try:
            user_input = float(input('argument: '))
            user_input2 = float(input('argument: '))
            answer = user_input / user_input2
            print(f'=> {answer}')
            # asking the user if wants to continue with another operation
            requesting_continuing()
        except ZeroDivisionError:
            print('Cannot divide by zero\n')
            #  restart if a zero division error
            division()
        except ValueError:
            print('Please type a number')
            #  restart if a value error
            division()


def multiply():
    while True:
        try:
            user_input = float(input('argument: '))
            user_input2 = float(input('argument: '))
            answer = user_input * user_input2
            print(f'=> {answer}')
            # asking the user if wants to continue with another operation
            requesting_continuing()
        except ValueError:
            print('Please type a number')
            #  restart if a value error
            multiply()


welcome()
