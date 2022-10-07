const { ipcRenderer } = require('electron')


ipcRenderer.on('prompt', function (evt, message) {
  document.getElementById("loader").style.display = "none";
  document.getElementById("prompt").style.display = "block";
  if (message.data[0].player == "black") {
    document.body.className = 'dark-theme';
  }
  if (message.data[0].player == "white") {
    document.body.className = 'light-theme';
  }
  document.getElementById("question").innerHTML = message.data[0].parameter;
});

function sendData() {
  let answer = document.getElementById("answer").value;
  document.getElementById("prompt").style.display = "none";
  document.getElementById("loader").style.display = "block";
  ipcRenderer.send('prompt-response', { answer });
};