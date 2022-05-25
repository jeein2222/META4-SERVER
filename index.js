const axios = require("axios");
const express = require("express");
const path = require("path");
const morgan = require("morgan");
const nunjucks = require("nunjucks");
const { sequelize } = require("./models");

const app = express();
app.set("port", process.env.PORT || 3001);
app.set("view engine", "html");
nunjucks.configure("views", {
  express: app,
  watch: true,
});
sequelize
  .sync({ force: false })
  .then(() => {
    console.log("데이터베이스 연결 성공");
  })
  .catch((err) => {
    console.error(err);
  });

app.use(morgan("dev"));
app.use(express.static(path.join(__dirname, "public")));
app.use(express.json());
app.use(express.urlencoded({ limit: "50mb", extended: false }));

//라우터
const imageRouter = require("./routes/Images");

app.use("/uploads", express.static("uploads"));
app.use("/api/image", imageRouter);

app.get('/', async (req, res) => {
  try{
      const response=await axios.post("http://localhost:5000/test",{content:"허수아비가"});
      console.log(response.data);
      res.status(201).json({result:"successPost"});
      res.send(response);
  }catch(error){

  }
});

app.listen(app.get("port"), () => {
  console.log(app.get("port"), "번 포트에서 대기 중");
});

