
import subprocess
from subprocess import call, PIPE, Popen
import sys

def runmain():
    subprocess.call('python Main.py')


#Pick a password
def pick_password():
        file = (r'C:\Users\Jeremy\Desktop\Launch Program\Login\FIles\pswd.txt')
        print ('Please pick a password.')
        password = input()
        target = open(file, 'w')
        target.write(password)
        file = (r'C:\Users\Jeremy\Desktop\Launch Program\Login\FIles\existence_check.txt')
        target = open(file, 'w')
        target.write('YES')
#       file.close()

#Function to check the password with the password located in pswd.txt
def password_check():
        file = (r'C:\Users\Jeremy\Desktop\Launch Program\Login\FIles\pswd.txt')
        pwd_check = open(file).read()
        userpass = input('Please input a password.\n')
        if userpass == pwd_check:
            print ('Password accepted!')
            sys.exit()
            runmain()
            sys.exit()
            
        elif userpass != pwd_check:
            print ('Sorry, wrong password.\n')
            sys.exit()
        else:
                print ('Invalid syntax.')
                sys.exit()

        
				



#location of password existence check file
EC = (r'C:\Users\Jeremy\Desktop\Launch Program\Login\FIles\existence_check.txt')
PWD = (r'C:\Users\Jeremy\Desktop\Launch Program\Login\FIles\pswd.txt') #Location of password file

pswd_exist = open(EC).read() #Checking to see if the password exists
if pswd_exist == 'YES':
        pass
else:
        pick_password() #If it doesn't, user will pick a password

#Checking for password
print ('looping or starting...\n')
password_check()