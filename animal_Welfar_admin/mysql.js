var fs = require('fs');
var mysql      = require('mysql');
//var MongoClient = require('mongodb').MongoClient;
var mysqldb;
mysqldb = {
    mysql_pool : mysql.createPool({
        host     : 'localhost',
        user     : 'sm6336',
        password : 'Qkrals9506!',
        database : 'test',
        port : 13307,
/*        ssl: {
                ca: fs.readFileSync(__dirname + '/keys/ca.pem'),
                key: fs.readFileSync(__dirname + '/keys/client-key.pem'),
                cert: fs.readFileSync(__dirname + '/keys/client-cert.pem')
        }*/
    })
};
module.exports = mysqldb;

