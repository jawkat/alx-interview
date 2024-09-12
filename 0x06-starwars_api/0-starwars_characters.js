#!/usr/bin/env node

const request = require('request');
const id = process.argv[2];

// Vérifie si l'utilisateur a fourni un ID de film
if (!id) {
  console.log("Usage: ./0-starwars_characters.js <Movie ID>");
  process.exit(1);
}

const findMovie = (id) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const data = JSON.parse(body);
    const charactersLinks = data.characters;
    const charactersPromises = charactersLinks.map((link) => {
      return new Promise((resolve, reject) => {
        request(link, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    });

    // Utiliser Promise.all pour attendre que tous les noms soient récupérés
    Promise.all(charactersPromises)
      .then((names) => {
        names.forEach((name) => console.log(name));
      })
      .catch((error) => {
        console.error('Error fetching characters:', error);
      });
  });
};

findMovie(id);
