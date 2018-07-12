import os

def cleanup():
	print('shutting down servers')
	os.system('killall npm')
	os.system('killall node')

def cleanupChrome():
	decision = input('would you like to automatically shutdown headless chrome?[Y][N] ')
	if decision.upper() == 'Y':
		os.system('killall chrome')
		print('This shut down all instances of chrome. Please reopen chrome to continue browing! ')
		 

cleanup()
cleanupChrome()

