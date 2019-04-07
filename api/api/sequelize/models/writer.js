/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('writer', {
    writer_id: {
      type: DataTypes.STRING(36),
      allowNull: false,
      primaryKey: true
    },
    kakao_id: {
      type: DataTypes.STRING(20),
      allowNull: false
    },
    kakao_name: {
      type: DataTypes.STRING(20),
      allowNull: false
    },
    email: {
      type: DataTypes.STRING(50),
      allowNull: false
    },
    phone: {
      type: DataTypes.STRING(20),
      allowNull: false
    }
  }, {
    tableName: 'writer',
    timestamps: false
  });
};
