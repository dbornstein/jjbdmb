import sys
import time
import random
import Login
import os




def cls():
	os.system('cls')


	pop_range_conventional = (0.0000002, 0.000001)
	pop_range_nuclear = (0.04, 0.10)
	
	
	

def main():
	global initial_pop_china
	initial_pop_china = int(1323000000)
	
	global initial_pop_russia
	initial_pop_india = int(146000000)
	
	
	
	
	
	
	
	
	
	
	global name
	cls()
	name = input("What is your title?  ")	
	cls()
	s = '\n' + 'Hello ' + name + ', don\'t do anything destructive.'
	print(s)


	
def actions():
	print ('\n')
	initial_action = input("Perform Action: ")
	action = initial_action.lower()
	
	
	
	if action == 'r' or action == 'restart':
		main()
		cls()
	elif action == 'speak' or action == 'talk' or action == 'say something':
		cls()
		phrase_to_cpu = input("Oh, put on the spot... What do you want me to say?")
		print (phrase_to_cpu.upper())
	elif action == 'power':
		sys.exit()
	elif action == 'hello':
		cls()
		hello = input('Hello ' + name + ', how are you?')
		if hello == 'good':
			print ("\nThat's good.")
			actions()
		else:
			print ("\nI am good,thanks for asking -_-")
	elif action == 'launch missile':
		cls()
		launch_missile()
			
	else:
		cls()
		p = '\nUnrecongnised statement: ' + initial_action
		print (p)
	
	actions()
	

	
	
def launch_missile():

	initial_type_of_missle = input("\nWhat type of missile do you wish to launch? \n\n:Conventional Guided:\n:Nuclear:\n=")
	type_of_missile = initial_type_of_missle.lower()
	
	cls()
	
	initial_target_country = input("What is the target country? \n\nCountry:     Population: \n China  -  1,323,000,000 \n Russia  -  146,000,000\n:")
	target_country = initial_target_country.lower()
	
	
	if type_of_missile == 'conventional guided' or type_of_missile == 'conventional':
		if target_country == 'china':
			cls()
			initial_confirm = input("Are you sure you want to do this? (yes / no)")
			confirm = initial_confirm.lower()
			if confirm == 'yes' or confirm == 'y':
			
				random_number = random.uniform(0.00000002, 0.0000001)
				casualties = initial_pop_russia * random_number
				
				cls()
				
				print("Launching Missile...")
				time.sleep(3)
				print("In Flight...")
				time.sleep(5)
				print("Impact. Gathering Results...")
				time.sleep(2)
				

				
				percent_of_population = random_number * 100
				printcasualties = casualties / 1000000
				j = "\n\nCasualtes: " + str(int(printcasualties)) + " million"
				k = (casualties * random.uniform(4.0, 7.0)) / 1000000
				l= "Other People Affected: " + str(int(k)) + " million\n\n"
				
				print(j)
				print("Percent of population killed: " + str('%.2f' % percent_of_population) + "%")
				print(l)
				time.sleep(2)
				actions()
				
			else:
				actions()
			
		elif target_country == 'russia':
			initial_confirm = input("Are you sure you want to do this? (yes / no)")
			confirm = initial_confirm.lower()
			if confirm == 'yes' or confirm == 'y':
			
				random_number = random.uniform(0.00000002, 0.0000001)
				casualties = initial_pop_russia * random_number
				
				
				print("Launching Missile...")
				time.sleep(3)
				print("In Flight...")
				time.sleep(5)
				print("Impact. Gathering Results...")
				time.sleep(2)
				
				
				percent_of_population = random_number * 100
				printcasualties = casualties / 1000000
				j = "\n\nCasualtes: " + str(int(printcasualties)) + " million"
				k = (casualties * random.uniform(4.0, 7.0)) / 1000000
				l= "Other People Affected: " + str(int(k)) + " million\n\n"
				
				print(j)
				print("Percent of population killed: " + str('%.2f' % percent_of_population) + "%")
				print(l)
				time.sleep(2)
				actions()
				
	elif type_of_missile == 'nuclear' or type_of_missile == 'nuclear missile':
	
		if target_country == 'china':
			cls()
			initial_confirm = input("\nAre you sure you want to do this? (yes / no)  ")
			confirm = initial_confirm.lower()
			if confirm == 'yes' or confirm == 'y':
			
			
				random_number = random.uniform(0.04, 0.10)
				casualties = initial_pop_china * random_number
				
				cls()
				
				print("Launching Missile...")
				time.sleep(3)
				print("In Flight...")
				time.sleep(8)
				print("Impact. Gathering Results...")
				time.sleep(2)
				
				percent_of_population = random_number * 100
				printcasualties = casualties / 1000000
				j = "\n\nCasualtes: " + str(int(printcasualties)) + " million"
				k = (casualties * random.uniform(4.0, 7.0)) / 1000000
				l= "Other People Affected: " + str(int(k)) + " million\n\n"
				
				print(j)
				print("Percent of population killed: " + str('%.2f' % percent_of_population) + "%")
				print(l)
				time.sleep(2)
				actions()
				
		elif target_country == 'russia':
			cls()
			initial_confirm = input("\nAre you sure you want to do this? (yes / no)  ")
			confirm = initial_confirm.lower()
			if confirm == 'yes' or confirm == 'y':
			
			
				random_number = random.uniform(0.04, 0.10)
				casualties = initial_pop_russia * random_number
				
				cls()
				
				print("Launching Missile...")
				time.sleep(3)
				print("In Flight...")
				time.sleep(8)
				print("Impact. Gathering Results...")
				time.sleep(2)
				
				percent_of_population = random_number * 100
				
				
				
				
				
				printcasualties = casualties / 1000000
				j = "\n\nCasualtes: " + str(int(printcasualties)) + " million"
				k = (casualties * random.uniform(4.0, 7.0)) / 1000000
				l= "Other People Affected: " + str(int(k)) + " million\n\n"
				
				print(j)
				print("Percent of population killed: " + str('%.2f' % percent_of_population) + "%")
				print(l)
				time.sleep(2)
				actions()
		





	
		
main()
actions()