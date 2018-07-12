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
    os.system('cd ./headless_chrome && chromium --headless --disable-gpu --remote-debugging-port=9222 & ')
    print('running headless chrome')
    os.system('node ./headless_chrome/app.js &')
    os.system('echo done')


copying()
# os.system(cmd)
# subprocess.call('npm run serve', shell=True)
# subprocess.call('cd ./headless_chrome && chromium --headless --remote-debugging-port=9222 --disable-gpu', shell=True)
# subprocess.call('cd node ./headless_chrome/app.js')
