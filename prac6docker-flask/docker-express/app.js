const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Hello express from docker!');
});

app.listen(3000, '0.0.0.0', () => {
    console.log('Express server running on port 3000');
});