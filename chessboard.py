#!/bin/python3
# Initial process that kicks off chessboard

# Import JSON to validate the opponents.json file
import json

# Import os for systemcalls
import os
import sys


def downloadStockfish():
    print("♟️  Downloading stockfish...")
    #stockfishUrl = ""
    #fileName = "stockfish"
    # with urllib.request.urlopen(stockfishUrl) as d:
    #    with open(os.path.realpath(f"chess_modules/stockfish_binary/{fileName}"), "wb+") as f:
    #        f.write(d.read())
    return True


def main():
    print("♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ Open-Source Smart Chessboard ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖")
    print("♟️  Checking for stockfish...")
    if not os.path.exists(os.path.realpath("./chess_modules/stockfish_binary/stockfish")):
        print("❌  Stockfish was not found")
        downloadStockfish()

    print("✔️  Setup complete")
    print("♟️  Running interface...")
    print()
    # Run the interface init script
    os.system(
        f"{sys.executable} {os.path.realpath(f'{os.path.dirname(__file__)}/interface/initialize.py')}"
    )

main()