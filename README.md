# OSSCB
Open-Source Smart Chessboard is a project with modularity in mind, which allows tinkerers to create their own smart chessboard. The board features automatic piece detection, starting games from custom positions with no hassle, software plugin support, a built-in chess clock, touchscreen controls and automatic recording of your games (in PGN-format). 

> keep in mind that this repo is not yet complete, and the project is still (both software and hardware wise) in heavy development. For more information about the way this software is developed, read the included readme's available in most directories. If updates are still visible in this README, that means I have not yet finalized the development process. But it's gonna be so cool once it's complete and I can't wait to share it.

By default, this software was written to deal with 64 RC522's (one per square), connected to a raspberry pi over I2C with 8 TCA9548A multiplexers. The LED-control is written for 144 fillament LED's (one on every edge of the squares), being controlled by TPIC6B595 shift registers (circuit will be available in this repo). The board and case for the raspberry pi will be 100% 3D-printable (STL-files will be available in this very repo), but feel free to make adjustments or use other materials. 

The heart of the project is a raspberry pi, running node.js and python. A chess clock, chess engine and plugin support are included by default, and the modular nature of the scripts allow for easy integration with your own sensors, switches, LEDSs and ideas. The backend is written in python, and the frontend is written in node.js on electron, so hopefully that simplifies the creation of your own code somewhat. I'll try and keep all the readme's and documents up-to-date.

Entrypoint of the chessboard is `chessboard.py` in the rootdirectory of the project. 

=== October update
As I am writing this, an order has been placed for all the components I need. Once I received everything I will update the repo again, since I wanna do the rest of my development on a raspberry pi. I am actively checking the repo though, so if you already find something you'd like to share your input on please let me know on twitter, @klepv1nk. I am not a developer by heart, so any feedback is appreciated (also I am looking for a cool name, anarchychess makes me wanna call the project knook but by the time that meme dies I'll regret it, so if you have any ideas also let me know).

If this update is still visible by the time you read this, that means the parts I ordered aren't in yet. I am working on it!