
import subprocess
from subprocess import call, PIPE, Popen
import sys
import os.path

PASSWDFILE='passwd.txt'

def runmain():
    subprocess.call('python Main.py')



#Pick a password
def pick_password():
        file = ('passwd.txt')
        password = input('Please enter a new password')
        target = open(file, 'w+')
        target.write(password)
        password_check()

#Function to check the password with the password located in pswd.txt
def password_check():

        if os.path.isfile(PASSWDFILE):
            password_check()
            userpass = target.read('passwd.txt')

        else:
            print("Password does not exist")		
            pick_password()




       
		
        if userpass == pwd_check:
            print ('Password accepted!')

            runmain()
            
        elif userpass != pwd_check:
            print ('Sorry, wrong password.\n')
            sys.exit()
        else:
                print ('Invalid syntax.')
                sys.exit()

        
			

