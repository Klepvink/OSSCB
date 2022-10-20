# Building the LED-system

The LED-system described here uses 144 filament LED's which can light up the edges on every square.

> **Please note** that this implementation can be time consuming and tedious. If you want to create the exact same chessboard as me feel free to follow the instructions. However, Feel free to make your own more efficient, cheaper or cooler implementation of the LED-system using different components. As long as there is a way for python to control your LED's, you can absolutely get your own solutions/ideas to work with OSSCB. Like any file in this project, I encourage you to write your own functions and code, and share that code with others. The documentation on how the LED-controller works (and how you can modify it to do whatever you want) can be found in the `/interface/` directory.

For building the LED-system you can use the following components:
- 18x 104 ceramic condensators
- 18x TPIC6B595 shift registers
> The more popular 74HC595's are (as far as I understand) not made to handle the power draw of these specific filament LED's. Unless you want to use other LED's that draw less, I would suggest you use the TPIC6B595's.
- 144x 54mm 3V filament LED's
> I opted to go with the 2700K white color due to me using wood, but honestly get whichever color you think would look cool with your material of choice (and share a picture with me on twitter if you do decide to build one, I wanna see what you come up with!)
- 144x 560 OHM (560R) resistors 
> the resistors determine the brightness of your LED's, but also determines the amount of power the LED's can draw from the power supply. The lower the resistance (ohms), the higher the brighness and power consumption. Keep in mind when determining the resistors you want to use that the filament LED's are really bright (they use these LED's in lightbulbs, two of these LED's can light an entire room and you are about to shove 144 of them in a chessboard) and draw a lot of power if you don't use the right resistor, so if you want your LED's to be brigher I would suggest you not to go below 330 OHM (330R). Keep in mind that you also need to power the raspberry pi using the same power supply.
- Plenty of wires and solderstuff
- Depending on how you want to wire it all together, probably a protoboard (which I will use aswell). However, if you have other ideas on how to neatly wire and implement this system in your own chessboard don't let me restrict you.
