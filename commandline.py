from shutil import copyfile
import os

def copying():
    headlessCMD = "cd ./headless_chrome && "
    file = input("What JSON do you want to use to generate the diagram? ")
    browser = int(input("Do you use Chromium[1] or Google Chrome[2](only enter the number)? "))
    original = './public/example-api.json'
    copyfile(file, original)
    if (browser == 1):
        headlessCMD += "chromium --headless --disable-gpu --hide-scrollbars --remote-debugging-port=9222 & "
        os.system('npm run serve &')
        os.system(headlessCMD)
        os.system('sleep 5 && node ./headless_chrome/screenshot.js && mv ./headless_chrome/output.jpeg ./output.jpeg && killall npm && killall node && killall chromium && echo "done"')
    elif (browser == 2):
        headlessCMD += "google-chrome --headless --disable-gpu --hide-scrollbars --remote-debugging-port=9222 & "
        os.system(headlessCMD)
        os.system('npm run serve &')
        os.system('sleep 10 && node ./headless_chrome/screenshot.js && mv ./headless_chrome/output.jpeg ./output.jpeg && killall npm && killall node && killall google-chrome && echo "done"')



copying()
