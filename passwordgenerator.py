import random

print('Welcome to myPasswordGenerator :')

data = 'qwertyuiop[]asdfghjkl;zxcvbm,<>* ABCDEFGHIJKLMNOPQRSTUVWXWZ()123456789'

choice1= input('Enter the length of the password :')
choice1=int(choice1)
print(' Here are your passwords: ')

#looping

passwords=''
for j in range(choice1):
    passwords += random.choice(data)
print(passwords)