var fs = require('fs')
var https = require('https')
var express = require('express');;
var cookieParser = require('cookie-parser')
var bodyParser = require('body-parser');
var router = express.Router();
var survey = require("./survey");
var result = require("./result")

var app = express();
app.use(cookieParser());
app.use(bodyParser.urlencoded({extended: false}));
/*
app.listen(5678, function(){
  console.log('server is running');
})
*/
https.createServer({
  key: fs.readFileSync('/etc/letsencrypt/live/www.mindpass.o-r.kr/privkey.pem'),
  cert: fs.readFileSync('/etc/letsencrypt/live/www.mindpass.o-r.kr/fullchain.pem'),
}, app).listen(5678, () => {
  console.log('Listening...')
})


app.post("/survey", survey.survey)
app.post("/result", result.result)
