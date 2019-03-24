/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('company', {
    comp_id: {
      type: DataTypes.CHAR(16),
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
