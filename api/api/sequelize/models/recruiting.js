/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('recruiting', {
    recr_id: {
      type: DataTypes.STRING(36),
      allowNull: false,
      primaryKey: true
    },
    writer_id: {
      type: DataTypes.STRING(36),
      allowNull: false,
      references: {
        model: 'writer',
        key: 'writer_id'
      }
    },
    type_id: {
      type: DataTypes.STRING(36),
      allowNull: false,
      references: {
        model: 'type',
        key: 'type_id'
      }
    },
    comp_id: {
      type: DataTypes.STRING(36),
      allowNull: false,
      references: {
        model: 'company',
        key: 'comp_id'
      }
    },
    title: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    content: {
      type: DataTypes.TEXT,
      allowNull: false
    },
    hit: {
      type: DataTypes.INTEGER(11),
      allowNull: false
    },
    cdate: {
      type: DataTypes.DATE,
      allowNull: false
    },
    udate: {
      type: DataTypes.DATE,
      allowNull: true
    },
    ddate: {
      type: DataTypes.DATE,
      allowNull: true
    },
    is_delete: {
      type: DataTypes.INTEGER(4),
      allowNull: false
    }
  }, {
    tableName: 'recruiting',
    timestamps: false
  });
};
