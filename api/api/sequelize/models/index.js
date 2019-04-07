'use strict';

const fs = require('fs');
const path = require('path');
const Sequelize = require('sequelize');
const basename = path.basename(__filename);
const env = process.env.NODE_ENV || 'development';
const config = require(__dirname + '/../config/config.json')[env];
const db = {};

const sequelize = new Sequelize(config.database, config.username, config.password, config);

fs
  .readdirSync(__dirname)
  .filter(function(file) {
    console.log(file)
    return (file.indexOf(".") !== 0) && (file !== "index.js");
  })
  .forEach(function(file) {
    var model = sequelize.import(path.join(__dirname, file));
    db[model.name] = model;
    console.log('model.name:' + model.name);
  });

Object.keys(db).forEach(function(modelName) {
  if ("associate" in db[modelName]) {
    db[modelName].associate(db);
  }
});

db.sequelize = sequelize;
db.Sequelize = Sequelize;
db.Op = Sequelize.Op;

db.Company = require('./company')(sequelize, Sequelize);
db.Detail = require('./detail')(sequelize, Sequelize);
db.Rating = require('./rating')(sequelize, Sequelize);
db.Recruiting = require('./recruiting')(sequelize, Sequelize);
db.Type = require('./type')(sequelize, Sequelize);
db.Writer = require('./writer')(sequelize, Sequelize);

db.Recruiting.belongsTo(db.Detail,  {foreignKey: 'recr_id',   targetKey: 'recr_id'});
db.Recruiting.hasMany(db.Company,   {foreignKey: 'comp_id',   sourceKey: 'comp_id'});
db.Recruiting.hasMany(db.Type,      {foreignKey: 'type_id',   sourceKey: 'type_id'});
db.Recruiting.hasMany(db.Writer,    {foreignKey: 'writer_id', sourceKey: 'writer_id'});

module.exports = db;
