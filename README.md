# OSSCB
Open-Source Smart Chessboard is a project with modularity in mind, which allows tinkerers to create their own smart chessboard. 

> keep in mind that this repo is not yet complete, and the project is still (both software and hardware wise) in heavy development. For more information about the way this software is developed, read the included readme's available in most directories.

By default, this software was written to deal with 64 rc522, connected to a raspberry pi over I2C over 8 TCA9548A multiplexers. The LED-control is written for 144 fillament LED's, being controlled by TPIC6B595 shift registers. The board is 100% 3D-printable (files will be available). The heart of the project is a raspberry pi, running node.js and python. A chess clock, chess engine and plugin support are included out-of-the-box, and the modular nature of the scripts allow for easy integration with your own sensors, switches, leds and ideas.

Entrypoint of the chessboard is `chessboard.py` in the rootdirectory of the project. 
