var auth = require("../helpers/auth");
const dbConfig = require('../helpers/db-config');
const Op = require('../sequelize/models').Op;
const Detail = require('../sequelize/models').Detail;
const Recruiting = require('../sequelize/models').Recruiting;
const Type = require('../sequelize/models').Type;
const Writer = require('../sequelize/models').Writer;
const Company = require('../sequelize/models').Company;
const moment = require('moment');

// DB Connection For Query
exports.listInsert = function(args, res, next) {
  
  var mysql = require('mysql');
  var connection = mysql.createConnection(dbConfig); 

  connection.query('SELECT * from board LIMIT 2;', function(err, rows, fields) {
    if (!err){
      return res.end(JSON.stringify(rows));
    } else {
      console.log('Error while performing Query.', err);
    }
  });
};


// DB Connection For ORM
exports.getRecruitDetail = function(args, res, next) {
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8'});
  var id = args.query.id ? args.query.id : '';
  
  Recruiting.findOne({
    attributes: ['title', 'content', 'hit', 'cdate', 'udate', 'ddate', 'is_delete'],
    where:{
      recr_id: id
    },
    include: [{model: Detail,  attributes: ['stock_opt', 'skill', 'url', 'period', 'price', 'years', 'sector', 'from_home', 'more_detail']},
              {model: Type,    attributes: ['type']},
              {model: Writer,  attributes: ['kakao_id', 'kakao_name', 'email', 'phone']},
              {model: Company, attributes: ['name', 'location']}]
  }).then((value) => {
    return res.end(JSON.stringify(value));
  });
};

// DB Connection For ORM
exports.getRecruitList = function(args, res, next) {
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8',
                      'Access-Control-Allow-Origin': '*'});
                      
  var condition = args.query.condition ? args.query.condition : '';

  const beforeDay = 60;
  var cdateCondition = new Date(Date.parse(new Date()) - beforeDay * 1000 * 60 * 60 * 24);
  cdateCondition = moment(cdateCondition.getFullYear() + '-' + (cdateCondition.getMonth() + 1) + '-' + cdateCondition.getDate(), 'YYYY-MM-DD');
  
  Recruiting.findAll({
    attributes: ['recr_id', 'title', 'content', 'hit', 'cdate', 'udate', 'ddate', 'is_delete'],
    where:{
      cdate: {
        [Op.gte]: cdateCondition
      }
    },
    order:[['cdate', 'DESC']],
    include: [{model: Detail,  attributes: ['stock_opt', 'skill', 'url', 'period', 'price', 'years', 'sector', 'from_home', 'more_detail']},
              {model: Type,    attributes: ['type']},
              {model: Writer,  attributes: ['kakao_id', 'kakao_name', 'email', 'phone']},
              {model: Company, attributes: ['name', 'location']}]
  }).then((value) => {
    value = value.map(v => {
      obj = {  dataValues: { recr_id: toHexString( Object.values(v.dataValues.recr_id)) }};
      v.dataValues.recr_id = toHexString( Object.values(v.dataValues.recr_id));
      debugger;
      return Object.assign(obj, v);
    })
    console.log(value)
    return res.end(JSON.stringify(value));
  });
};

function toHexString(byteArray) {
  return Array.from(byteArray, function(byte) {
    return ('0' + (byte & 0xFF).toString(16)).slice(-2);
  }).join('')
}
