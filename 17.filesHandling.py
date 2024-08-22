'''
Using python functions to read, write and append a file.
'''
with open('write.py', 'w') as file:
    file.write('This is Sai\n')
          
with open('write.py', 'r') as file:
    content=file.read()
    
print(content)

with open('write.py', 'a') as file:
    file.write('This is Trinadh\n')
          
with open('write.py', 'r') as file:
    content=file.read()
    
print(content)

with open('write.py', 'a') as file:
    file.write('This is Trinadh Sai\n')
          
with open('write.py', 'r') as file:
    content=file.read()
    
print(content)
