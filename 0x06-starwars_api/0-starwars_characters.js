#!/usr/bin/env node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;
request(apiUrl, (err, res, body) => {
  if (err) {
    console.error('Error fetching film data:', err);
    return;
  }
  const characterUrls = JSON.parse(body).characters;
  fetchCharactersInOrder(characterUrls, 0);
});

const fetchCharactersInOrder = (urls, index) => {
  if (index === urls.length) {
    return;
  }
  request(urls[index], (err, res, body) => {
    if (err) {
      console.error('Error fetching character data:', err);
      return;
    }
    console.log(JSON.parse(body).name);
    fetchCharactersInOrder(urls, index + 1);
  });
};
