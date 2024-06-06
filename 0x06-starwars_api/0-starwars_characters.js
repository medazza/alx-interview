#!/usr/bin/node
const http = require("https");
const API_ENDPOINT = "https://swapi-api.hbtn.io/api";

if (process.argv.length > 2) {
  const filmId = process.argv[2];
  fetchFilmCharacters(filmId)
    .then((characterNames) => console.log(characterNames.join("\n")))
    .catch((error) => console.error(error));
}

function fetchFilmCharacters(filmId) {
  return new Promise((resolve, reject) => {
    http
      .get(`${API_ENDPOINT}/films/${filmId}/`, (response) => {
        let data = "";
        response.on("data", (chunk) => {
          data += chunk;
        });
        response.on("end", () => {
          const { characters } = JSON.parse(data);
          Promise.all(characters.map(fetchCharacterName))
            .then(resolve)
            .catch(reject);
        });
      })
      .on("error", reject);
  });
}

function fetchCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    http
      .get(characterUrl, (response) => {
        let data = "";
        response.on("data", (chunk) => {
          data += chunk;
        });
        response.on("end", () => {
          resolve(JSON.parse(data).name);
        });
      })
      .on("error", reject);
  });
}
