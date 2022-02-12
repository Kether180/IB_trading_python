const express = require('express');
const { spawn } = require('child_process');

const app = express();

app.get('/', (req, res) => {
   console.log('Hello world');
});


app.get('/', (req, res) => {
    const childPython = spawn('python', ['order.py']);
 
    childPython.stdout.on('data', (data) => {
       console.log(`stdout: ${data}`)
    });
 
    childPython.stderr.on('data', (data) => {
       console.error(`stderr: ${data}`);
    });
 
    childPython.on('close', (code) => {
       console.log(`child process exited with code ${code}`);
    });
 });

app.listen(3000, console.log('Server started on port 3000'));