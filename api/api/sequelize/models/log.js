/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('log', {
    log_id: {
      type: "BINARY(16)",
      allowNull: false,
      primaryKey: true
    },
    recr_id: {
      type: "BINARY(16)",
      allowNull: false,
      references: {
        model: 'recruiting',
        key: 'recr_id'
      }
    },
    timestamp: {
      type: DataTypes.DATE,
      allowNull: false
    },
    type: {
      type: DataTypes.STRING(3),
      allowNull: false
    },
    ip: {
      type: DataTypes.STRING(100),
      allowNull: false
    }
  }, {
    tableName: 'log',
    timestamps: false
  });
};
