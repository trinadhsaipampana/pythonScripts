'''
Declare 2 conditions with nested-if to check eligibility ot vote
'''

age=int(input("What is your age: \n"))

if age >= 18:
    
    id=input("\nDo you have valid id(Yes/No):\n")
    
    if id == 'Yes':
        
        print(f'\nYou are eligible to vote')
    else:
        print(f'\nGet valid id to vote')
    
else:
    
    print(f'\nYou are not eligible to vote')