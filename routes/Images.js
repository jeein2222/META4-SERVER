const express = require("express");
const router = express.Router();
const { Images } = require("../models");
const multer = require("multer");
const fs = require("fs");
const path = require("path");

router.get("/", async (req, res) => {
  const listImages = await Images.findAll();
  res.json(listImages);
});

router.get("/:id", async (req, res) => {
  const id = req.params.id;
  const image = await Images.findByPk(id);
  res.json(image);
});

try {
  fs.readdirSync("uploads");
} catch (error) {
  //upload폴더가 없을시 생성
  fs.mkdirSync("uploads");
}

const upload = multer({
  storage: multer.diskStorage({
    destination(req, file, cb) {
      //서버에 저장될 위치
      cb(null, "uploads/");
    },
    filename(req, file, cb) {
      const ext = path.extname(file.originalname);
      //서버에 저장될 때 파일 이름
      cb(null, path.basename(file.originalname, ext) + Date.now());
    },
  }),
  limits: { fileSize: 5 * 1024 * 1024 },
});

//이미지 업로드 API
//upload의 single 메서드는 하나의 이미지를 업로드할 때 사용
router.post("/", upload.single("drawImg"), async (req, res) => {
  const drawImg = req.file.path;
  //각종 예외처리 생략

  const all = await Images.create({
    drawImg,
  });
  res.json(all);
});

module.exports = router;
