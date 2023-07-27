const apiUrl = "http://127.0.0.1:5000"

const jsonData = {"team": "white"}

function start_game(){

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
  console.log(data);
})
.catch(error => {
  // Handle errors
  console.error('Error:', error);
});


document.getElementById("output").innerHTML = data;


}