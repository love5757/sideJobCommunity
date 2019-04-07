/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('company', {
    comp_id: {
      type: DataTypes.STRING(36),
      allowNull: false,
      primaryKey: true
    },
    name: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    location: {
      type: DataTypes.STRING(150),
      allowNull: false
    }
  }, {
    tableName: 'company',
    timestamps: false
  });
};
