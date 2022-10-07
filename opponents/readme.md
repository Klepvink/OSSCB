# Opponent component developer reference

> This guide is written for developers that want to create their own implementation of the open-source smart chessboard. This board features sensors which can detect pieces (and their location) automatically, has a system for LED-control using standard chess notation, and has code written with modularity in mind which hopefully helps other tinkerers to build their own version of the chessboard with other physical components. Since every module and class communicates using standard chess notation/data, you can easily implement your own code and swap out existing functions for other ones.

Opponent components are python files with a class inside of them, which are programmed to output chess moves. These classes must have a function to get chessboard data, and a function that outputs a chess move (in UCI notation).

You could create an opponent that allows a player to play with someone online, play against a certain engine, or implement some other cool way to play chess.

## Creating an opponent component

### Placing your opponent component
opponent components are expected to be placed in the `/opponents` directory in the root of the project directory. This folder already includes two sample files: an opponent which prompts a (probably) real person for his moves and decisions through the console (called `console.py`), and an opponent which uses stockfish to determine certain moves (called `machine.py`). Place your python file in this directory. 

> **Please note** that your filename (minus the `.py` file extension) is expected to have the same name as the python class within the file. For example, the `console.py` opponent has a class which is called `console`. Mind the usage of upper/lowercase letters.

### Registering your opponent component
In order for the application to be aware of your component, it must be registered in the `/opponents.json` file located in the root of the project directory. Registering your component works as follows:
Append a new JSON-object to the file. Make sure you don't forget the comma if you do this manually). This data is as follows:
```
{
"name": // Enter your componentname here, make sure it is a string //,
"description": // Feel free to add a description here, make it a string //,
"classname": // Enter the name of your opponent class (your filename without .py), also a string //,
"parameters": [// This is a list of parameters your component needs in order for it to work. The player will be prompted to enter this information //]
}
```
After that, you're done! Your component is registered and ready to be used.

## Mandatory functions

> :warning: **Please note** that these functions must be named **exactly** like they are stated here. If this is not the case, the game might make a call to a non-existent function (which is not good).

These functions are mandatory to have in your class, to make sure the game is able to interact with your opponent component. You are however free to create your own functions besides these mandatory ones. These are purely used/called to interact with the game.

### pass_boardstate
the `pass_boardstate` function of your class is always called when it is your turn to move. This call includes a FEN-formatted string which resembles the current state of the game. This script should contain logic that saves this state, for when a move needs to be made by the player. For example, this function can write the string to `self.boardstate` to use it for analysis in another function.

Returning a `True` (boolean) on success or a `False` (boolean) in case of failure is advised after this function is called. The game does not expect any data from the component. 

### get_move
the `get_move` function of your class is always called when the component is expected to make a move in the game. This function is not called with any data. However, the component is expected to return a string containing a chess move in UCI notation. 

You could use this function to ask the player to enter his move (see the `console.py` opponent), use an engine to analyze the current state of the board, or write any other logic here that determines the move that the component wants to make. As long as the function returns a string with a move (in UCI notation), you're good. 

## Working with user preferences

If opponent component is registered with parameters, the player is asked to provide that data. After the player gave an answer to these parameters, this data is collected into a python dictionary. The keynames are the name of the parameter (as defined in `opponents.json`), and the value is the answer the player gave. After that, your component is initiated and is passed this dict. You can use this dict to get the parameters you need.

It's recommended to have an `__init__` function inside of your class, which takes a dictionary as input. This dictionary can then be saved to `self.settings` (or whatever name you think sounds cool) to make it accessible to other functions within that specific instance of your component. 

## That's it!

Hope this provided you with enough information to start creating your own virtual chess player. Feel free to poke in the other opponents, and if you write anything cool please let me know, I'd love to know about it. My twitter is @klepv1nk.