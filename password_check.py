correct_password = 'python'
password = input('Enter password: ')

while password != correct_password:
    password = input('Wrong password, try again: ')

print('Logged in!')