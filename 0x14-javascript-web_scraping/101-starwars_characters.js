#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

function doRequest (url) {
  return new Promise((resolve, reject) => {
    req(url, (error, res, body) => {
      if (!error && res.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

req.get(url + id, async (error, res, body) => {
  if (error) {
    console.log(error);
  }
  for (const character of JSON.parse(body).characters) {
    console.log(JSON.parse(await doRequest(character)).name);
  }
}
);
