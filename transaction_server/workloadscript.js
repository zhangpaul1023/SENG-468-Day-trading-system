import http from 'k6/http';

export default function () {
  function randomSymbol() {
    function randomLetter() {
      const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      return alphabet[Math.floor(Math.random() * alphabet.length)];
    }
    return `${randomLetter()}${randomLetter()}${randomLetter()}`;
  }
  const params = {
	  timeout:'3600s'
  };
  const user = `user${__VU}`;
  const host = 8000 + (__VU%3);
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const symbol = `${alphabet[Math.floor(Math.random() * alphabet.length)]}${alphabet[Math.floor(Math.random() * alphabet.length)]}${alphabet[Math.floor(Math.random() * alphabet.length)]}`;
  
  for (;;){
	  var res = http.get(`http://localhost:${host}/transactions/create_user/${user}/`,params); 
  	  if (res.status != 408 && res.status < 500) {
	  	break;
	  }
  }
  http.get(`http://localhost:${host}/transactions/add/${user}/63511.53/`,params); 
  http.get(`http://localhost:${host}/transactions/quote/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/276.83/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/quote/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/add/${user}/45016.23/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/display_summary/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/add/${user}/71879.98/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/303.83/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/add/${user}/74315.15/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_buy/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/51.49/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/156.07/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/575.27/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/display_summary/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/set_buy_amount/${user}/${symbol}/658.38/`,params); 
  http.get(`http://localhost:${host}/transactions/sell/${user}/${symbol}/641.90/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_sell/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/264.17/`,params); 
  http.get(`http://localhost:${host}/transactions/quote/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/657.49/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/display_summary/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/710.47/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/208.11/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/display_summary/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/add/${user}/52802.93/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/433.22/`,params); 
  http.get(`http://localhost:${host}/transactions/set_sell_trigger/${user}/${symbol}/59.23/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/387.59/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_buy/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_buy/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/display_summary/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/quote/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/quote/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/sell/${user}/${symbol}/429.74/`,params); 
  http.get(`http://localhost:${host}/transactions/set_sell_trigger/${user}/${symbol}/51.92/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/384.67/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/357.57/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/set_sell_amount/${user}/${symbol}/216.83/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_sell/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/516.29/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/sell/${user}/${symbol}/41.47/`,params); 
  http.get(`http://localhost:${host}/transactions/set_sell_trigger/${user}/${symbol}/30.04/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_buy/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_sell/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/289.68/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_buy/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/add/${user}/87863.73/`,params); 
  http.get(`http://localhost:${host}/transactions/quote/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/333.91/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/sell/${user}/${symbol}/213.24/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/427.36/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/730.08/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/36.79/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/sell/${user}/${symbol}/644.65/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_sell/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_sell/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_set_sell/${user}/${symbol}/`,params); 
  http.get(`http://localhost:${host}/transactions/buy/${user}/${symbol}/749.86/`,params); 
  http.get(`http://localhost:${host}/transactions/commit_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/cancel_buy/${user}/`,params); 
  http.get(`http://localhost:${host}/transactions/sell/${user}/${symbol}/664.10/`,params); 
  //http.get(`http://localhost:${host}/transactions/dumplog/./testlog`,params); 
}
