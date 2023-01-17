#!/usr/bin/node

const fs = require('fs');
const argOne = process.argv[2];
const argTwo = process.argv[3];
fs.writeFileSync(argOne, argTwo, 'utf-8', (error, log) => {
  if (error) {
    console.log(error);
  } else {
    console.log(log);
  }
});
