const { app, BrowserWindow, ipcMain } = require('electron')
const xmlrpc = require('xmlrpc')

// Create the window
const createWindow = () => {
    const server = xmlrpc.createServer({ host: 'localhost', port: 9090 });

    const win = new BrowserWindow({

        // The app is supposed to be fullscreen, for ✨ seamless ✨ look
        fullscreen: true,
        autoHideMenuBar: true,
        webPreferences: {

            // To make sure node.js code can run from the renderer, enable nodeIntegration
            nodeIntegration: true,
            contextIsolation: false,
        }
    });

    // Load the first page
    win.loadFile('index.html');

    // Hide the cursor, just in case. This application is meant for touchscreens
    win.webContents.on('dom-ready', (event) => {
        let css = '* { cursor: none !important; }';
        win.webContents.insertCSS(css);
    });

    // If a call through XMLRPC is not found, deal with it appropriately
    server.on('NotFound', function (method, params, callback) {
        callback("not found");
    })

    // Simple ping-pong, for the pythoncode to determine if frontend has succesfully started
    server.on('ping', function (err, params, callback) {
        callback(null, "pong");
    });

    // Deal with a promptcall, asking the player to enter information
    server.on('prompt', function (err, params, callback) {
        win.loadFile('prompt.html');
        win.webContents.on("dom-ready", (event) => {
            win.webContents.send('prompt', { 'data': params });
        });
        // When the data returns from the frontend, pass it through to the chessboard
        ipcMain.on("prompt-response", (event, message) => {
            callback(null, message);
        });
    });
    server.on('update', function (err, params, callback) {
        callback(null, "true")
        win.loadFile('update.html');
        win.webContents.on("dom-ready", (event) => {
            win.webContents.send('prompt', { 'data': params });
        });
    });
}

// Start the application when ready
app.whenReady().then(() => {
    createWindow();
})

// Close the application appropriately when requested
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
})