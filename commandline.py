from shutil import copyfile
import os
from subprocess import Popen, PIPE

def copying():
    file = input("What JSON do you want to use to generate the diagram? ")
    original = './public/example-api.json'
    copyfile(file, original)
    cmd = "diff " + file + " " + original
    os.system(cmd)

    os.system('npm run serve &')
    print('running npm server')
    browser = "Do you use Google Chrome[1] or Chromium[2](only enter the number)? "
    if (browser == 1):
    	os.system('cd ./headless_chrome && chromium --headless --disable-gpu --remote-debugging-port=9222 & ')
    elif (browser == 2):
    	os.system('cd ./headless_chrome && google-chrome --headless --disable-gpu --remote-debugging-port=9222 & ')
	
    print('running headless chrome')
    os.system('node ./headless_chrome/app.js &')
    os.system('echo done')


copying()
