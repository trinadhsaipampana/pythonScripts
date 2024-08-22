'''
Declare a function to call welcome greeting for student with name,branch as arguments
Provide hobbies as dynamic arguments
Provide details as key-pairs
'''

def WELCOME(name, branch='JNIT'):
    print('*'*20)
    print(f'Hi {name}')
    print(f'Your branch is:\n{branch}')
    
def INTERESTS(*hobbies):
    print(f'Your interests are:')
    for hobby in hobbies:
        print(hobby)

def DETAILS(**info):
    print(f'Your details are:')
    for key,value in info.items():
        print(f'{key} is {value}')

'''    
WELCOME('Sai', 'EEE')
INTERESTS('singing', 'dancing', 'running', 'trekking')
DETAILS(DOB='21st Feb 1995', POB='Mandapeta')

WELCOME('Trinadh', 'ECE')
INTERESTS('reading', 'swimming', 'basket ball')
DETAILS(DOB='7th May 1996', POB='Kakinada')

WELCOME('Krishna')
INTERESTS('wating news','cricket', 'volley ball')
DETAILS(DOB='9th April 1998', POB='Amalapuram')
'''