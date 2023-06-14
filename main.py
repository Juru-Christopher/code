#!/user/bin/python3
import operations as op
import sys

for i in range(5):
    tmpVal = op.welcomeScreen()
    if tmpVal == 1:
        op.adminLogin()
        break
    elif tmpVal == 2:
        op.userLogin()
        break
    elif tmpVal == 3:
        op.help()
        break
    elif tmpVal == 4:
        print("Bye Bye\nExiting...")
        sys.exit(1)
    else:
        print("Invalid Operation!\nTry Again")
        if i == 5:
            print("Service Timeout")
