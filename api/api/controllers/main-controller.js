var auth = require("../helpers/auth");
const dbConfig = require('../helpers/db-config');
const Sequelize = require('../sequelize/models').Sequelize;
const sequelize = require('../sequelize/models').sequelize;
const Op = require('../sequelize/models').Op;
const Detail = require('../sequelize/models').Detail;
const Recruiting = require('../sequelize/models').Recruiting;
const Type = require('../sequelize/models').Type;
const Writer = require('../sequelize/models').Writer;
const Company = require('../sequelize/models').Company;
const moment = require('moment');

// Insert Company
exports.insertCompany = function(args, res, next) {
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8',
                      'Access-Control-Allow-Origin': '*'});
                      
  var comp_id = args.body.comp_id || getUUID();
  var name = args.body.name;
  var location = args.body.location;

  var obj = {
    comp_id,
    name,
    location
  }
  
  Company.create(obj).then(function(result) {
    return res.end(JSON.stringify({status: 'success'}));
  }).catch(function(err) {
    return res.end(JSON.stringify({status: 'error', reason: err}));
  });
};

// Insert Writer
exports.insertWriter = function(args, res, next) {
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8',
                      'Access-Control-Allow-Origin': '*'});

  var writer_id = args.body.writer_id || getUUID();
  var kakao_id = args.body.kakao_id;
  var kakao_name = args.body.kakao_name;
  var email = args.body.email;
  var phone = args.body.phone;

  var obj = {
    writer_id,
    kakao_id,
    kakao_name,
    email,
    phone
  }
  
  Writer.create(obj).then(function(result) {
    return res.end(JSON.stringify({status: 'success'}));
  }).catch(function(err) {
    return res.end(JSON.stringify({status: 'error', reason: err}));
  });
};

// Insert Type
exports.insertType = function(args, res, next) {
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8',
                      'Access-Control-Allow-Origin': '*'});

  var type_id = args.body.type_id || getUUID();
  var type = args.body.type;

  var obj = {
    type_id,
    type
  }
  
  Type.create(obj).then(function(result) {
    return res.end(JSON.stringify({status: 'success'}));
  }).catch(function(err) {
    return res.end(JSON.stringify({status: 'error', reason: err}));
  });
};

// Insert Recruiting
exports.insertRecruiting = function(args, res, next) {
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8',
                      'Access-Control-Allow-Origin': '*'});
  
  var recruiting = {
    recr_id: args.body.recr_id || getUUID(),
    writer_id: args.body.writer_id || 'a64d31c576f94910885782b0cf733cd4',
    type_id: args.body.type_id || '34f0179659504ce09120e29603d1ec46',
    comp_id: args.body.comp_id || '8045798cf5a143efaf829c4154660f0a',
    title: args.body.title,
    content: args.body.content,
    hit: args.body.hit || 0,
    cdate: Sequelize.fn('NOW'),
    is_delete: args.body.is_delete || 0
  }

  var detail = {
    stock_opt: args.body.stock_opt,
    skill: args.body.skill,
    url: args.body.url,
    period: args.body.period,
    price: args.body.price,
    years: args.body.years,
    sector: args.body.sector,
    from_home: args.body.from_home,
    more_detail: args.body.more_detail
  }
  
  sequelize.transaction({autocommit:false}).then(function(t) {
    return Recruiting.create(recruiting, {transaction: t}).then(function(recruiting) {
      detail.recr_id = recruiting.recr_id;
  
      return Detail.create(detail, {transaction: t}).then(function(detail) {
        t.commit();
        return res.end(JSON.stringify({status: 'success'}));
      })
  
    }).catch(function(err) {
      t.rollback();
      return res.end(JSON.stringify({status: 'error', reason: err}));
    });
  });
};


// DB Connection For ORM
exports.getRecruitDetail = function(args, res, next) {
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8',
                      'Access-Control-Allow-Origin': '*'});
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
    return res.end(JSON.stringify(value));
  });
};

function getUUID() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  }
  return s4() + s4() + s4() + s4() + s4() + s4() + s4() + s4();
}
