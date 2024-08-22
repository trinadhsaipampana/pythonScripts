'''
Use try and except method to avoid termination of program on errors.
'''

num1=10
num2=0

print(f'product {num1*num2}')
try:
    print(f'Division {num1/num2}')
except:
    ZeroDivisionError
print(f'Difference {num1-num2}')
print(f'Sum {num1+num2}')