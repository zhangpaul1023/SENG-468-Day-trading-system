import http from 'k6/http';

const ENTRY = 0;
const QUOTE = 1;
const ADD = 2;
const DISPLAY_SUMMARY = 3;
const TRANSACTION = 4;
const CANCEL = 5;
const COMMIT = 6;
const EXIT = 7

export default function () {
  function randomSymbol() {
    function randomLetter() {
      const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      return alphabet[Math.floor(Math.random() * alphabet.length)];
    }
    return `${randomLetter()}${randomLetter()}${randomLetter()}`;
  }
  function randomNumer() {
    return Math.floor(Math.random() * 100);
  }

  let state = ENTRY;
  const user = `user${__VU}`;
  let symbol = randomSymbol();
  let rand = 0;
  http.get(`http://localhost:8000/transactions/create_user/${user}/`);

  while(state != EXIT) {
    switch(state) {
      case ENTRY:
        rand = randomNumer();
        if (rand < 34) {
          state = ADD;
        } else if (rand < 68) {
          state = QUOTE;
        } else {
          state = DISPLAY_SUMMARY;
        }
        break;
      case QUOTE:
        rand = randomNumer();
        symbol = randomSymbol();
        http.get(`http://localhost:8000/transactions/quote/${user}/${symbol}/`);
        if (rand < 25) {
          state = QUOTE;
        } else if (rand < 50) {
          state = DISPLAY_SUMMARY;
        } else if (rand < 75) {
          state = ADD;
        } else {
          state = TRANSACTION;
        } 
        break;
      case ADD:
        rand = randomNumer();
        http.get(`http://localhost:8000/transactions/add/${user}/0.00/`);
        if (rand < 50) {
          state = QUOTE;
        } else {
          state = ADD;
        }
        break;
      case DISPLAY_SUMMARY:
        rand = randomNumer();
        //http.get(`http://localhost:8000/transactions/display_summary/${user}/`);
        if (rand < 50) {
          state = QUOTE;
        } else {
          state = EXIT;
        }
        break;
      case TRANSACTION:
        rand = randomNumer();
        http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/0.00/`);
        if (rand < 50) {
          state = COMMIT;
        } else {
          state = CANCEL;
        }
        break;
      case CANCEL:
        rand = randomNumer();
        http.get(`http://localhost:8000/transactions/cancel_buy/${user}/`);
        if (rand < 50) {
          state = DISPLAY_SUMMARY;
        } else {
          state = QUOTE;
        }
        break;
      case COMMIT:
        randomNumer();
        http.get(`http://localhost:8000/transactions/commit_buy/${user}/`);
        if (rand < 50) {
          state = DISPLAY_SUMMARY;
        } else {
          state = QUOTE;
        }
        break;
      default:
    }
  }

}
