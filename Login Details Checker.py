# Login Details Checker - Hands on coding for beginners
# username = ade   password = 12345
import time
# Declaring Global variables
username1 = 'ade'
password1 = '12345'
passcount = 0
while True and passcount < 3:
    passcount += 1
    # Prompt to receive password from user
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    # Comparing entered values with the predefined value
    if username == username1 and password1 == password:
        print('Please wait...')
        time.sleep(5)
        print('Matching data values in progress...')
        time.sleep(3)
        print('Login Successful')
        print('You\'re logged in, Please wait while we pull up your account data:....')
        break
    else:
        # To be perfomed when the wrong username and password is entered
        print('Please wait...')
        time.sleep(5)
        print('Matching data values in progress...')
        time.sleep(3)
        print('You Entered the wrong login details, try again')
else:
    # To be performed after three trials for entering the correct details is exausted.
    print('Please wait...')
    time.sleep(3)
    print('You\'ve exausted all three attempt, contact the admin')
