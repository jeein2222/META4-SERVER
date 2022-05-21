//이미지를 저장하는 Model

module.exports = (sequelize, DataTypes) => {
  const Images = sequelize.define("Images", {
    drawImg: {
      type: DataTypes.BLOB("long"),
      allowNull: false,
    },
  });

  return Images;
};
