#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const part = process.argv[2];

async function getChar (part) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + part + '/';
  let response = await (await request(url)).body;
  response = JSON.parse(response);
  const chars = response.characters;

  for (let i = 0; i < chars.length; i++) {
    const charUrl = chars[i];
    const charResp = await (await request(charUrl)).body;
    const character = JSON.parse(charResp);
    console.log(character.name);
  }
}

getChar(part);
