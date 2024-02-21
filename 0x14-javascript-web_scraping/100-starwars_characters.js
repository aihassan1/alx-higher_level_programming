#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

// Make a request to the provided URL
request(url, (error, response, body) => {
  // Handle errors
  if (error) {
    console.error('Error:', error);
    return;
  }
});
console.log(body);
