# Chess modules

> This guide is written for developers that want to create their own implementation of the open-source smart chessboard. This board features sensors which can detect pieces (and their location) automatically, has a system for LED-control using standard chess notation, and has code written with modularity in mind which hopefully helps other tinkerers to build their own version of the chessboard with other physical components. Since every module and class communicates using standard chess notation/data, you can easily implement your own code and swap out existing functions for other ones.

The `/chess_modules` folder contains handy chess-related modules that may be used by any module, class or function within the project. These modules can be used to do certain chess-related actions, like calculating the move that was made by comparing two different FEN-strings, or validate certain data. 

> **Please note** if you are developing your own plug-ins, opponents or alternative code (and you are planning to share your changes with the world (which you should totally do)), please do not add new modules here. Instead, include the dependencies/functions you need within your python-file. The reason you should not do this, is to make sure it is as easy as possible for users to swap/add code and opponents to their game by just dragging and dropping a file. Having to install and add multiple files and dependencies might make this process more difficult, and/or cause problems. However, if you think the existing modules can be improved, feel free to do so and share your changes with the world (but respect the expected in- and output of the modules/functions to ensure your code is compatible with the other modules and functions that rely on this module).

## Modules

### Stockfish binary
The `./stockfish_binary` folder contains a compiled version of stockfish for the appropriate platform. Please note that this binary is downloaded from the official stockfish website when the chessboard is booted (since I am not comfortable shipping compiled code with my project when claiming its open-source and I do not want to force players to compile code themselves). The stockfish binary is simply called `/chess_modules/stockfish_binary/stockfish` (`stockfish.exe` if you are on Windows (though I should probably note that I really do recommend your running your chessboard using a raspberry pi running raspberry pi OS lite)). 

### FenDiff (fendiff.py)
FenDiff (`/chess_modules/fendiff.py`) is a python script that is capable of finding a made move by comparing two FEN-strings. This script is mainly used to translate chessboard-states to moves. These moves can then be passed into the running game by an opponent component (read `/opponents/readme.md`). Importing the function can be done by adding `from chess_modules/fendiff import fendiff`. The fendiff functions expects 2 FEN-formatted strings, and returns a chess-move in UCI-format (string). 

