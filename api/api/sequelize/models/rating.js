/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('rating', {
    recr_id: {
      type: "BINARY(16)",
      allowNull: false,
      primaryKey: true,
      references: {
        model: 'recruiting',
        key: 'recr_id'
      }
    },
    merit: {
      type: DataTypes.INTEGER(11),
      allowNull: false
    }
  }, {
    tableName: 'rating'
  });
};
