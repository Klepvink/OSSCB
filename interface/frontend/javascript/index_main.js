var xmlrpc = require('xmlrpc');
const { Splide } = require('@splidejs/splide');

let path = "../../opponents.json";
const fs = require('fs');
const json = JSON.parse(fs.readFileSync(path));

var client = xmlrpc.createClient({ host: 'localhost', port: 8000, path: '/' });

var blackScroller = document.querySelector('.chess-black');
var whiteScroller = document.querySelector('.chess-white');

var whiteOpponent = "";
var blackOpponent = "";

const boxes = document.querySelectorAll('.splide__list');
for (const box of boxes) {
    for (var i = 0; i < json.length; i++) {
        var obj = json[i];
        box.innerHTML += `<li chess-data="${obj['name']}" class="splide__slide"><p class="menu-text">${obj['name']}</p></li>`
    }
}

new Splide('#splide-left', {
    type: 'loop',
    drag: 'free',
    snap: true,
    direction: 'ttb',
    height: '100%',
    perPage: 3,
    focus: 'center',
}).mount().on('scrolled', function () {
    blackOpponent = blackScroller.querySelector(".is-active").getAttribute("chess-data");
});

new Splide('#splide-right', {
    type: 'loop',
    drag: 'free',
    snap: true,
    direction: 'ttb',
    height: '100%',
    perPage: 3,
    focus: 'center',
}).mount().on('scrolled', function () {
    whiteOpponent = whiteScroller.querySelector(".is-active").getAttribute("chess-data");
});

function CreateGame() {
    client.methodCall('chess_game', [whiteOpponent, blackOpponent], function (error, value) {
    });
}