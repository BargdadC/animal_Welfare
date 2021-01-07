var client = require("./mysql.js").mysql_pool;

exports.insert = function(req,res){
  var scope_list = req.body.scope_list;
  var category = req.body.category;
  var info = req.body.info;

  client.query('insert into result_info (scope_list, category, info) values (?, ?, ?)',[scope_list, category, info],function(err, result){
    if(err){
      res.json({code:500});
      console.log(err)
    }else{
      console.log('insert success')    //쓰기성공
      //res.json({code:210})
      res.redirect(req.get('referer'));
    }
  })
}

