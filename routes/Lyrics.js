const express = require("express");
const router = express.Router();
const axios = require("axios");

router.post("/", async (req, res) => {
  try {
    const response = await axios.post("http://localhost:5000/test", {
      content: "허수아비가",
    });
    console.log(response.data);
    res.status(201).json({ result: "successPost" });
    res.send(response);
  } catch (error) {
    console.log("분석할수없습니다.");
  }
});

module.exports = router;
