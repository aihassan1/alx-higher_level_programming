#!/usr/bin/node
const path = process.argv[2];
const fs = require('fs');

const data = fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
