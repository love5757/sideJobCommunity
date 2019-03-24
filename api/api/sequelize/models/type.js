/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('type', {
    type_id: {
      type: DataTypes.CHAR(16),
      allowNull: false,
      primaryKey: true
    },
    type: {
      type: DataTypes.STRING(20),
      allowNull: false
    }
  }, {
    tableName: 'type',
    timestamps: false
  });
};
