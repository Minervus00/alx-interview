#!/usr/bin/node
// Prints all characters of a Star Wars movie which id is given as parameter

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const result = JSON.parse(body).characters;

    result.forEach(char => {
      request(char, (err, resp, bdy) => {
        if (!err) {
          console.log(JSON.parse(bdy).name);
        }
      });
    });
  }
});
