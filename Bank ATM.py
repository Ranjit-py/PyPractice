print('Welcom to Patil Bank of India ATM')
restart = ('Y')
chances = 3
balance = 100
while chances >= 0:
    pin = int(input('Please Enter Your Pin: '))
    if pin == (1234):
        print('You entered Pin correctly\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Press 1 to Check your Balance\n')
            print('Press 2 for Withdrawl\n')
            print('Press 3 to Pay in\n')
            print('Press 4 to Return Card\n')
            option = int(input('What would you like to choose? '))
            if option == 1:
                print('Your Balance is ', balance, '\n')
                restart = input('Would you like to go back? ')
                if restart in ('n', 'N', 'NO', 'no'):
                    print('Thank you')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How much would you like to withdraw? \n'))
                if withdrawl in [10, 20, 30, 50, 80, 90, 100]:
                    balance = balance - withdrawl
                    print('\nYour balance is now ', balance)
                    restart = input('Would you like ot go back? ')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank you')
                        break
                elif withdrawl != [10, 20, 30, 50, 80, 90, 100]:
                    print('Invalid Amount, Pls Retry\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Pls Enter Amount: '))

            elif option ==3:
                pay_in = float(input('How Much Would You Like to Pay In? '))
                balance = balance + pay_in
                print('\nYour Balance is now', balance)
                restart = input('Would You Like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait while you card is Returned...\n')
                print('Thank you for banking with us')
                break
            else:
                print('Please enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break
