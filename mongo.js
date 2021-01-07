var MongoClient = require('mongodb')
var url = "mongodb://localhost:27018/animal_Welfare";
var db;

module.exports.connect = function connect(callback) {
    MongoClient.connect(url, function(err, conn){
        /* exports the connection */
        module.exports.db = conn.db('animal_Welfare'); //database명을 명시했다.;
        callback(err);
    });
};
