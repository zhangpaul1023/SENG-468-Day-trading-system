import http from 'k6/http';

export default function () {
  function randomSymbol() {
    function randomLetter() {
      const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      return alphabet[Math.floor(Math.random() * alphabet.length)];
    }
    return `${randomLetter()}${randomLetter()}${randomLetter()}`;
  }

  const user = `user${__VU}`;
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const symbol = `${alphabet[Math.floor(Math.random() * alphabet.length)]}${alphabet[Math.floor(Math.random() * alphabet.length)]}${alphabet[Math.floor(Math.random() * alphabet.length)]}`;
  http.get(`http://localhost:8000/transactions/create_user/${user}/`);
  http.get(`http://localhost:8000/transactions/add/${user}/63511.53/`); 
  http.get(`http://localhost:8000/transactions/quote/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/276.83/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/quote/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/add/${user}/45016.23/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  //http.get(`http://localhost:8000/transactions/display_summary/${user}/`); 
  http.get(`http://localhost:8000/transactions/add/${user}/71879.98/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/303.83/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/add/${user}/74315.15/`); 
  http.get(`http://localhost:8000/transactions/cancel_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_buy/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/commit_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/51.49/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/156.07/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/575.27/`); 
  http.get(`http://localhost:8000/transactions/cancel_sell/${user}/`); 
  //http.get(`http://localhost:8000/transactions/display_summary/${user}/`); 
  http.get(`http://localhost:8000/transactions/set_buy_amount/${user}/${symbol}/658.38/`); 
  http.get(`http://localhost:8000/transactions/sell/${user}/${symbol}/641.90/`); 
  http.get(`http://localhost:8000/transactions/commit_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_sell/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/commit_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/264.17/`); 
  http.get(`http://localhost:8000/transactions/quote/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/657.49/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  //http.get(`http://localhost:8000/transactions/display_summary/${user}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/710.47/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/208.11/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  //http.get(`http://localhost:8000/transactions/display_summary/${user}/`); 
  http.get(`http://localhost:8000/transactions/add/${user}/52802.93/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/433.22/`); 
  http.get(`http://localhost:8000/transactions/set_sell_trigger/${user}/${symbol}/59.23/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/387.59/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_buy/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_buy/${user}/${symbol}/`); 
  //http.get(`http://localhost:8000/transactions/display_summary/${user}/`); 
  http.get(`http://localhost:8000/transactions/quote/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/quote/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/sell/${user}/${symbol}/429.74/`); 
  http.get(`http://localhost:8000/transactions/set_sell_trigger/${user}/${symbol}/51.92/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/384.67/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/357.57/`); 
  http.get(`http://localhost:8000/transactions/cancel_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/set_sell_amount/${user}/${symbol}/216.83/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_sell/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/516.29/`); 
  http.get(`http://localhost:8000/transactions/cancel_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/sell/${user}/${symbol}/41.47/`); 
  http.get(`http://localhost:8000/transactions/set_sell_trigger/${user}/${symbol}/30.04/`); 
  http.get(`http://localhost:8000/transactions/commit_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_buy/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_sell/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/289.68/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_buy/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/add/${user}/87863.73/`); 
  http.get(`http://localhost:8000/transactions/quote/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/333.91/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/sell/${user}/${symbol}/213.24/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/427.36/`); 
  http.get(`http://localhost:8000/transactions/cancel_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/730.08/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/36.79/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/sell/${user}/${symbol}/644.65/`); 
  http.get(`http://localhost:8000/transactions/cancel_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_sell/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/cancel_sell/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_set_sell/${user}/${symbol}/`); 
  http.get(`http://localhost:8000/transactions/buy/${user}/${symbol}/749.86/`); 
  http.get(`http://localhost:8000/transactions/commit_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/cancel_buy/${user}/`); 
  http.get(`http://localhost:8000/transactions/sell/${user}/${symbol}/664.10/`); 
  //http.get(`http://localhost:8000/transactions/dumplog/./testlog`); 
}