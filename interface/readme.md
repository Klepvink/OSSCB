# Interface

> This guide is written for developers that want to create their own implementation of the open-source smart chessboard. This board features sensors which can detect pieces (and their location) automatically, has a system for LED-control using standard chess notation, and has code written with modularity in mind which hopefully helps other tinkerers to build their own version of the chessboard with other physical components. Since every module and class communicates using standard chess notation/data, you can easily implement your own code and swap out existing functions for other ones.

The `/interface` folder contains the first script (`/interface/initialize.py`) that is called after the chessboard checks (ha-ha) if the required files are in the right spot, accessible, updates are pulled (if internet connection is available) and any neccesary binaries are downloaded/available. The interface folder should contain code that allows the user to create a new game/interact with the "smart" functions of the chessboard. This folder and it's contents are very abstract. By default it will contain code that will interact with a touchscreen, but you can swap it out with for example a simple CLI-tool, a flask webserver that makes it possible to control the chessboard from a web interface, or create an API and write a front-end in your favorite language.

## Useful information for developers

### Initiating a game
To create a game, you can call the `chess_game` function from `/game.py` (importing `chess_game` from `/game.py` should work fine). This function takes (two) opponent names (read `/opponents/readme.md`) as strings. The game will then be created.

### Providing a list of opponents
To provide the user with a list of opponents the player can play against, the file can interpret the `/opponents.json` file located in the root of the project directory (make sure to import the `json` module in the script that is responsible for interpreting that file). 

## Modules

### The initialize file (initialize.py)
This file is executed after the chessboard is finished booting. This contains logic that exposes an interface to the user of the chessboard, from which the user is able to control it.

### Prompting a user (prompt.py)
This function (`prompt`) is called by the game whenever a bit of information is needed. The function must be able to accept two strings, which player needs to have the information (either `"white"` or `"black"`) and the bit of information needed. This information is used to prompt the user of the chessboard to give the data that is needed. This function should return a string.

### Getting a game update (update.py)
This function (`update`) is called by the game whenever it is someone elses turn. This function should accept two strings, the player who's turn it now is (either `"white"` or `"black"`) and the state of the board (in FEN-format). This information could be used to create a chess clock, get stockfish to run analysis after a move using the positions on the board, or to simply keep track of who's turn it is. Returning data is not neccesary or expected, but it is adviced to return a boolean (`True`) just in case.

> If you need to determine what move was made for your purposes, you can use the `fendiff.py` function inside of `chess_modules/fendiff.py`. For more information, read `/chess_modules/readme.md`.
