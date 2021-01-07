var client = require("./mysql.js").mysql_pool;

exports.update = function(req,res){
  var scope_list = req.body.scope_list;
  var category = req.body.category;
  var info = req.body.info;
  var bbsid = parseInt(req.body.bbsid);
  //console.log(req.body);

  client.query('update result_info set scope_list = ?, category = ?, info = ? where bbsid = ?',[scope_list, category, info, bbsid],function(err, result){
    if(err){    //db연결오류
      res.json({code:500})
      console.log(err)
    }else{      //게시판 부르기성공
      res.redirect('/info/1');
      console.log('update success')
    }
  })
}
