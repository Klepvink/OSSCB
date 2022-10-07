import os

class machine(object):
    # The machine class creates an instance of stockfish, the open source chess engine
    # https://github.com/zhelyabuzhsky/stockfish

    # Initialize the information
    def __init__(self, settingsDict):

        # Define path to the stockfish executable
        stockfish_path = os.path.realpath("chess_modules/stockfish_binary/stockfish")

        # Check for a valid ELO
        if int(settingsDict["Stockfish ELO"]) < 100:
            raise ValueError(
                f"Stockfish ELO attribute must be set to a integer above 100")

        if (settingsDict["player_color"].lower() != "white") and (settingsDict["player_color"].lower() != "black"):
            raise ValueError(
                f"player_color attribute must be set to either \"white\" or \"black\"")

        # Set the stockfish values
        self.player_elo = int(settingsDict["Stockfish ELO"])
        self.player_color = settingsDict["player_color"]

        self.Stockfish = __import__("stockfish").Stockfish
        self.stockfish = self.Stockfish(path=stockfish_path, depth=int(settingsDict["Stockfish depth"]), parameters={
            "Threads": 4, "Minimum Thinking Time": int(settingsDict["Stockfish minimum thinking time"])})

        self.stockfish.set_elo_rating(self.player_elo)
        print(self.stockfish.get_parameters())

    # Give stockfish the current state of the board, to be called after every turn
    def pass_boardstate(self, boardstate):

        if self.stockfish.is_fen_valid(boardstate):
            self.boardstate = boardstate
            self.stockfish.set_fen_position(self.boardstate)

            return True
        else:
            return False

    def get_move(self):
        if self.boardstate:
            return self.stockfish.get_best_move()
