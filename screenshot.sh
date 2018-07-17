#!/bin/bash
npm run serve &
sleep 10 && cd ./headless_chrome && google-chrome-stable --headless --disable-gpu --hide-scrollbars --remote-debugging-port=9222 http://localhost:8080/ &
sleep 20 && node ./headless_chrome/screenshot2.js
