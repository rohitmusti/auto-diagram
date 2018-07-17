#!/bin/bash

echo 'hello world'
npm run serve & 
cd ./headless_chrome && google-chrome-stable --headless --disable-gpu --hide-scrollbars --remot-debuggingport=9222 &
sleep 10 && node ./headless_chrome/screenshot.js && mv./headless_chrome/output.jpeg ./output.jpeg && killall npm && killall chrome && echo 'done'
