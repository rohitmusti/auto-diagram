from shutil import copyfile
import os

def copying():
    # headlessCMD = "cd ./headless_chrome && "
    file = input("What JSON do you want to use to generate the diagram? ")
    # browser = int(input("Do you use Chromium[1] or Google Chrome[2](only enter the number)? "))
    original = './public/example-api.json'
    copyfile(file, original)
    # if (browser == 1):
    #     headlessCMD += "sleep 10 && chromium --headless --node-sandbox --disable-gpu --hide-scrollbars --remote-debugging-port=9222 & "
    #     os.system('npm run serve &')
    #     os.system(headlessCMD)
    #     os.system('sleep 20 &&  node ./headless_chrome/screenshot2.js && mv ./headless_chrome/output.jpeg ./output.jpeg && killall npm && killall node && killall chromium && echo "done"')
    # elif (browser == 2):
    #     headlessCMD += "sleep 10 && google-chrome-stable --headless --disable-gpu --hide-scrollbars --remote-debugging-port=9222 & "
    #     os.system('npm run serve &')
    #     os.system(headlessCMD)
    #     os.system('sleep 20 && node ./headless_chrome/screenshot2.js && mv ./headless_chrome/output.jpeg ./output.jpeg && killall npm && killall node && killall chrome && echo "done"')



copying()
