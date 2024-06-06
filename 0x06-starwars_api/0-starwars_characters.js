#!/usr/bin/node
const request = require("request");
const API_URL = "https://swapi-api.hbtn.io/api";

function fetchFilmCharacterNames(filmId) {
  return new Promise((resolve, reject) => {
    request(`${API_URL}/films/${filmId}/`, (err, _, body) => {
      if (err) {
        reject(err);
      } else {
        const characterUrls = JSON.parse(body).characters;
        Promise.all(characterUrls.map(fetchCharacterName))
          .then(resolve)
          .catch(reject);
      }
    });
  });
}

function fetchCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (err, _, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

if (process.argv.length > 2) {
  const filmId = process.argv[2];
  fetchFilmCharacterNames(filmId)
    .then((names) => console.log(names.join("\n")))
    .catch((error) => console.error(error));
}
