#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));

const fetchCharacters = async () => {
  const args = process.argv.slice(2);
  if (args.length === 0) return;
  try {
    const movieReq = await request(`https://swapi-api.alx-tools.com/api/films/${args[0]}`);
    const charactersUrls = await JSON.parse(movieReq.body).characters;
    if (!charactersUrls) return;
    for (const characterUrl of charactersUrls) {
      const characterReq = await request(characterUrl);
      const character = await JSON.parse(characterReq.body);
      console.log(character.name);
    }
  } catch (error) {
    return error;
  }
};

fetchCharacters();
