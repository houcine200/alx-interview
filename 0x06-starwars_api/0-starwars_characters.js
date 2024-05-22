#!/usr/bin/env node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// URL for fetching the movie data
const url = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie data
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  // Fetch and print each character name
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
