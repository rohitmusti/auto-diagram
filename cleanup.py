import os

def cleanup():
	print('shutting down servers')
	os.system('killall npm')
	os.system('killall node')

def cleanupChrome():
	decision = int(input('Would you like to automatically shutdown headless chrome?["1" if using chromium]["2" if using chrome]["3" if no] '))
	if decision == '1':
		os.system('pkill -f "(chromium)?(--headless)"')
		os.system('killall chromium')
		print('This shut down all instances of chromium. Please reopen chromium to continue browing! ')
	elif decision == '2':
		os.system('pkill -f "(chrome)?(--headless)"')
		os.system('killall google-chrome')
		print('This shut down all instances of google chrome. Please reopen google chrome to continue browing! ')
	else:
		print('Finished!')


cleanup()
cleanupChrome()
