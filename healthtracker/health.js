const express = require("express");
const axios = require("axios");

const app = express();
app.use(express.json());

let healthdatas = [];

app.get("/healthtracker", (req, res) => {
    res.json(healthdatas);
});

app.post("/healthcare", (req, res) => {
    const healthdata = {
        id: healthdatas.length + 1,
        title: req.body.title,
        duration: req.body.duration
    };

    healthdatas.push(healthdata);

    axios.post("http://127.0.0.1:5000/todos", {
        task: req.body.title,
        status: "Done"
    });

    res.status(201).json({
        message: "Health record added successfully!",
        healthdata: healthdata
    });
});

app.listen(3000, () => {
    console.log("Health Tracker API running on port 3000");
});