const apiUrl = "http://127.0.0.1:5000"

const jsonData = { "team": "white" }

var pythonData;

var output = document.getElementById("output");

function start_game() {

  fetch(apiUrl + "/start", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(jsonData)
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response from the server
      pythonData = data;
      console.log(pythonData);
      output.innerHTML = pythonData;
    })
    .catch(error => {
      // Handle errors
      console.error('Error:', error);
    });

}


function move_piece() {
  console.log(pythonData.boardString);

  output.innerHTML += "<br><br><br>" + pythonData.boardString;

}