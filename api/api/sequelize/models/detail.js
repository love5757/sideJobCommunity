/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('detail', {
    recr_id: {
      type: DataTypes.INTEGER(11),
      allowNull: false,
      primaryKey: true
    },
    stock_opt: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    skill: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    url: {
      type: DataTypes.TEXT,
      allowNull: false
    },
    period: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    price: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    years: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    sector: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    from_home: {
      type: DataTypes.INTEGER(1),
      allowNull: true
    },
    more_detail: {
      type: DataTypes.TEXT,
      allowNull: false
    }
  }, {
    tableName: 'detail',
    timestamps: false
  });
};
