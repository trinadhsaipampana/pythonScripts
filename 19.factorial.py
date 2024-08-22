'''
Get a number from user and calculate factorial of that number
'''

Num=int(input('Enter a number:\n'))

def factorial(Num):
    return 1 if Num==1 else Num*factorial(Num-1)

print(factorial(Num))