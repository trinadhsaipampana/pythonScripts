'''
Declare a list of users and perform some listing operations
'''

userList=[ "sai", "ravi", "laxmi", "prakash" ]

print(f'Users in the list are:\n{userList}\n')

print(f'Second user in the list is:\n{userList[1]}\n')

print(f'Adding new user prasanthi at the end of the list')

userList.append('prasanthi')

print(userList)

print(f'\nDeleting prasanthi from list')

userList.remove('prasanthi')

print(userList)

print(f'\nReplacing laxmi with lakshmi in the list')

userList[2]='lakshmi'

print(userList)

print(f'\nInserting krishna at index 2')

userList.insert(2,'krishna')

print(userList)

print(f'\nDeleting user at index 2')

del userList[2]

print(userList)

print(f'\nLength of the list is: {len(userList)}')