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


// Insert Recruiting
exports.insertRecruiting = function(args, res, next) {
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8'});
  
  var company = {
    comp_id: getUUID(),
    name: args.body.name,
    location: args.body.location
  }

  var writer = {
    writer_id: getUUID(),
    kakao_id: args.body.kakao_id,
    kakao_name: args.body.kakao_name,
    email: args.body.email,
    phone: args.body.phone
  }

  var type = {
    type_id: getUUID(),
    type: args.body.type
  }

  var recruiting = {
    recr_id: getUUID(),
    writer_id: writer.writer_id,
    type_id: type.type_id,
    comp_id: company.comp_id,
    title: args.body.title,
    content: args.body.content,
    hit: 0,
    cdate: Sequelize.fn('NOW'),
    is_delete: 0
  }

  var detail = {
    recr_id: recruiting.recr_id,
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
    return Company.create(company, {transaction: t}).then(function(company) {
      return Writer.create(writer, {transaction: t}).then(function(writer) {
        return Type.create(type, {transaction: t}).then(function(type) {
          return Recruiting.create(recruiting, {transaction: t}).then(function(recruiting) {
            return Detail.create(detail, {transaction: t}).then(function(detail) {
              t.commit();
              return res.end(JSON.stringify({status: 'success'}));
            })
          })
        })
      })
    }).catch(function(err) {
      t.rollback();
      return res.end(JSON.stringify({status: 'error', reason: err}));
    });
  });
};


// Update View
exports.updateHit = function(args, res, next) {
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8;'});
  var id = args.body.recr_id;

  Recruiting.findOne({
    attributes: ['hit'],
    where:{
      recr_id: id
    }
  }).then((value) => {
    Recruiting.update({
      hit: value.hit + 1
    }, {
      where: { recr_id: id }
    })
    .then(() => {
      return res.end(JSON.stringify({status: 'success'}));
    });
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
  res.writeHead(200, {'content-type':'application/json; charset=UTF-8'});
  
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
