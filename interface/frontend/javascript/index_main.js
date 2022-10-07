var xmlrpc = require('xmlrpc')

var client = xmlrpc.createClient({ host: 'localhost', port: 8000, path: '/' })

function CreateGame() {
    client.methodCall('chess_game', ['Machine', 'Machine'], function (error, value) {
    });
}