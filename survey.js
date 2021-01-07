var mongo = require("./mongo.js")
var util = require("util")

exports.survey= function(req,res,next){
  var name = req.body.name;
  var tel = req.body.tel;
  var age = req.body.age;
  var num_of_sample = req.body.num_of_sample;
  var num_of_all = req.body.num_of_all;
  var category = req.body.category;
  var data = req.body.data;
  var objData = JSON.parse(data)
  mongo.connect(function(err){
    if(err) throw err;
    var date = new Date();
    date.setHours(date.getHours()+9);
    mongo.db.collection('survey').insert({name:name, tel:tel, age:age, num_of_sample:num_of_sample, num_of_all:num_of_all,category:category, data:objData, date:date},function(err,doc){
      if(err){
        res.json({code:500});
        console.log(err);
      }else{
//        console.log('insert success')    //쓰기성공
//        res.json({code:210})
          console.log(tel)
          var spawn = require("child_process").spawn;
          var process = spawn('python3',["/home/sm6336/animal_Welfare/result.py",tel]);
          process.stdout.on('data', function(data){
            var result2 = JSON.stringify(data.toString());
            var result = JSON.parse(result2);
            var test=JSON.parse(data.toString());
            res.json(test);
            console.log(test)
          })
      }
    })
  })
}
