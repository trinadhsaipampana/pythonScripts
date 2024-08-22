'''
Declare a key-value pair of subject and marks in dictionary
'''

subMarks={ 'Telugu':88, 'Hindi':75, 'English':78, 'Maths':89, 'Science':95, 'Social':97 }

print(f'All subject marks:')

print(subMarks)

print(f'\nTelugu marks:')

print(subMarks['Telugu'])

print(f'\nAdding PS and NS marks')

subMarks['PS']=48

subMarks['NS']=47

print(subMarks)