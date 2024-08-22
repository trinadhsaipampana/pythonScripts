'''
Get a num from user and check wheather it is even or odd
'''

userInput=""

while userInput != 'q':
    userInput=input(f'Provide a number or q to quit: \n')
    if userInput.isdigit():
        if int(userInput)%2 == 0:
            print(f'Number is even')
        else:
            print(f'Number is odd')