from shutil import copyfile
import os

def copying():
    headlessCMD = ""
    file = input("What JSON do you want to use to generate the diagram? ")
    browser = int(input("Do you use Chromium[1] or Google Chrome[2](only enter the number)? "))
    original = './public/example-api.json'
    copyfile(file, original)
    if (browser == 1):
    	headlessCMD = 'cd ./headless_chrome && chromium --headless --disable-gpu --remote-debugging-port=9222 & '
    elif (browser == 2):
    	headlessCMD = 'google-chrome --headless --disable-gpu --remote-debugging-port=9222 & '

    # print(headlessCMD)
    os.system('npm run serve &')
    os.system(headlessCMD)
    os.system('sleep 5 && node ./headless_chrome/screenshot.js &')
    # os.system('echo done')


copying()
