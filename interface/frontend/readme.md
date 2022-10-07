### The frontend

The frontend of the chessboard is an electron application in full screen. The reason for this is because electron gives the developer to use web technologies to create a cool-looking application, it allows the application to deal with animations and touch in a smooth way, and using XMLRPC it makes for easy integration with python. It is of course not a solution as tightly intergrated with python like tkinder or QT, but for a touchscreen application it should be fine.

If you don't want to run an electron-application, feel free to make edits or write your own frontend (read `/interface/readme.md`). I'd love to see what you come up with!