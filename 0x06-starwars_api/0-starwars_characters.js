#!/usr/bin/env node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if a movie ID is provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// SWAPI films endpoint
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Request the film data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching film data:', error);
    return;
  }

  // Parse the response body
  const filmData = JSON.parse(body);

  // Check if the movie exists
  if (response.statusCode !== 200) {
    console.error('Movie not found');
    return;
  }

  // Get the list of character URLs
  const characters = filmData.characters;

  // Fetch and print each character's name in order
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
