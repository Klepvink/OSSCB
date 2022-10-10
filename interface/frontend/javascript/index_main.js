var xmlrpc = require('xmlrpc');
const { Splide } = require('@splidejs/splide');

var client = xmlrpc.createClient({ host: 'localhost', port: 8000, path: '/' });

new Splide('#splide-left', {
    type: 'loop',
    drag: 'free',
    snap   : true,
    direction: 'ttb',
    height   : '100%',
    perPage: 3,
}).mount();

new Splide('#splide-right', {
    type: 'loop',
    drag: 'free',
    snap   : true,
    direction: 'ttb',
    height   : '100%',
    perPage: 3,
}).mount();

function CreateGame() {
    client.methodCall('chess_game', ['Machine', 'Machine'], function (error, value) {
    });
}