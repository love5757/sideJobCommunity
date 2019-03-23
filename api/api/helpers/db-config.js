"use strict";

exports.db_conn = function() {
  var mysql      = require('mysql');
  var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'manager',
    password : 'Javascript',
    port     : 3306,
    database : 'sidejob_proj'
  });
};