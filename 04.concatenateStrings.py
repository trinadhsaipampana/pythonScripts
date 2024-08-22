'''
Get first name, second name and last name from the user aand concatenate them together to print full name
'''

firstName=input("Provide the first name:\n")

secondName=input("\nProvide the second name:\n")

lastName=input("\nProvide the last name:\n")

fullName=firstName + ' ' + secondName + ' ' + lastName

print(f'\nMy name is {firstName}\n')

print(f'My full name is {fullName}')