const express = require('express');
const mongoose = require('mongoose');

const app = express();

mongoose.connect('mongodb://mongo:27017/mydb')
    .then(() => console.log('MongoDB Connected'))
    .catch(err => console.log(err));

app.get('/', (req, res) => {
    res.send('Express + MongoDB using Docker Compose');
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});