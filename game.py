# Import the chess package for basic chess functions and rules
import chess
import chess.pgn

# Import the JSON-module to interpret the opponents.json file
import json

# Import custom modules
from interface.prompt import prompt
from interface.update import update

def chess_game(white, black):
    
    # Read the opponents.json file to get more information about available opponents
    with open("opponents.json", "r") as f:
        data = json.load(f)

    for i in data:

        # First initialize the white player
        if white == i['name']:
            print("♟️  Class found in definitions, initializing...")

            # Import the file (to be named the same as the class) into a module
            whiteOpponentModule = getattr(__import__(
                f"opponents.{i['classname']}"), f"{i['classname']}")

            # Get the class from the loaded module
            whitePlayerClass = getattr(whiteOpponentModule, i['classname'])

            print("♟️  Class initalized, gathering settings...")
            whiteSettingsDict = {}
            for s in i["parameters"]:
                
                # Prompt for answers to defined variables
                whiteSettingsDict.update({s: prompt("white", s)})

            # Set the opponents color
            whiteSettingsDict.update({"player_color": "white"})

            # Pass the settings as a dictionary to the class, initiate the class
            whitePlayer = whitePlayerClass(whiteSettingsDict)

        # Then initialize the black player
        if black == i['name']:
            print("♟️  Class found in definitions, initializing...")

            # Import the file (to be named the same as the class) into a module
            blackOpponentModule = getattr(__import__(
                f"opponents.{i['classname']}"), f"{i['classname']}")

            # Get the class from the loaded module
            blackPlayerClass = getattr(blackOpponentModule, i['classname'])

            print("♟️  Class initalized, gathering settings...")
            blackSettingsDict = {}
            for s in i["parameters"]:
                
                # Prompt for answers to defined variables
                blackSettingsDict.update({s: prompt("black", s)})

            # Set the opponents color
            blackSettingsDict.update({"player_color": "black"})

            # Pass the settings as a dictionary to the class, initiate the class
            blackPlayer = blackPlayerClass(blackSettingsDict)

    #### After getting and setting the players, start the game and PGN recording
    # Create/initialize a chessboard
    board = chess.Board()

    # Create a game (for PGN recording)
    game = chess.pgn.Game()

    game.headers["Event"] = "Chess game"
    game.headers["White"] = "White"
    game.headers["Black"] = "Black"

    # Setup the game according to board layout
    game.setup(board)

    # Init node (because the docs told me to)
    node = game
    while not board.is_game_over():

        update("white", board.fen())
        ## Keep in mind that the move order is hard-coded (white first), and the FEN-information is not interpreted to 
        ## see who's turn it is.

        # Give white player information about the board
        whitePlayer.pass_boardstate(board.fen())
        
        # Prompt white player for moves
        whiteMove = whitePlayer.get_move()
        board.push_san(whiteMove)
        node = node.add_variation(chess.Move.from_uci(whiteMove))
        
        # If the game is over after the turn, escape the gameloop
        if board.is_game_over():
            break
        
        update("black", board.fen())
        # Give black player information about the board
        blackPlayer.pass_boardstate(board.fen())

        blackMove = blackPlayer.get_move()
        board.push_san(blackMove)
        node = node.add_variation(chess.Move.from_uci(blackMove))

    print(board.fen())
    game.headers["Result"] = board.result()
    print(game)