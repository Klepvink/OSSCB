class console(object):
    # Simple opponent based on user input

    # Initialize the information
    def __init__(self, settingsDict):

        if (settingsDict["player_color"].lower() != "white") and (settingsDict["player_color"].lower() != "black"):
            raise ValueError(
                f"player_color attribute must be set to either \"white\" or \"black\"")

        # Set the values
        self.player_color = settingsDict["player_color"]

    # Give the player the current state of the board, to be called after every turn
    def pass_boardstate(self, boardstate):

        self.boardstate = boardstate
        return True

    # Get the move played by the player
    def get_move(self):
        if self.boardstate:
            # Return a string based on the user input
            return input("Enter your move > ")

