#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const ActorId = 18;
const TargetLink = `https://swapi-api.alx-tools.com/api/people/${ActorId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const results = data.results;

  let count = 0;

  results.forEach((item) => {
    if (item.characters.includes(TargetLink)) {
      count++;
    }
  });
  console.log(count);
});
