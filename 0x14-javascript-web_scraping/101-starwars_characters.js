#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
req.get(url + id, (error, res, body) => {
  if (error) {
    console.log(error);
  }
  for (const i of JSON.parse(body).characters) {
    req.get(i, (error, res, body1) => {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body1).name);
    });
  }
});
