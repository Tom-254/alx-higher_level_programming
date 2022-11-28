#!/usr/bin/node
const argNum = process.argv[2];

if (isNaN(argNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argNum; i++) {
    let square = '';
    for (let j = 0; j < argNum; j++) {
      square = square + 'X';
    }
    console.log(square);
  }
}
