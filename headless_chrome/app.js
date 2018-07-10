var screenshot = require('./screenshot.js')
var express = require('express')
var app = express()

// respond with "hello world" when a GET request is made to the homepage
app.get('/', function (req, res) {
  screenshot();
  res.sendFile(__dirname + '/output.jpeg')
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))
