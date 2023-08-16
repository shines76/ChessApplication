
const apiUrl = "http://127.0.0.1:5000"
const jsonData = { "team": "white" }
const x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"];
const y_axis = [1, 2, 3, 4, 5, 6, 7, 8]

async function onClickPlay() {

  try {
    let data = await getChessData();
    console.log(data.boardString);
    return data;
  } catch (error) {

    console.error('Error', error);

  }

}

const pythonData = onClickPlay();

async function buildBoard() {

}
async function buildTiles() {


  //return [{{xy}, {"piece"}}, ...]

}

async function setBoard(boardString) {
  return {
    boardString,
    tiles: buildTiles(),
    buildBoard: function () {


    }
  }
}

const board = setBoard(pythonData.boardString,)



async function getChessData() {
  try {
    const response = await fetch(apiUrl + "/start", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(jsonData)
    });
    const data = await response.json();
    return data;
  } catch (error) {
    throw error;
  }
}

async function move_piece() {
  console.log(pythonData.boardString);

  output.innerHTML += "<br><br><br>" + pythonData.boardString;

}

