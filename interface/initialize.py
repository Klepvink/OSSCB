import os
from xmlrpc import client
from xmlrpc.server import SimpleXMLRPCServer
from pynpm import NPMPackage
import sys
import time

# Import the chess_game function
sys.path.append(os.path.abspath('.'))
import game

def main():
    print("♟️  Starting RPC-server in backend...")
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_function(game.chess_game, "chess_game")
    print("✔️  Server started!")
    server.serve_forever()

def initializeFrontend():
    print("♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ OSSCB Frontend ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖")
    # Set DISPLAY to make sure electron is executed on the display
    # I am not sure if this actually does anything, but I am more comfortable leaving it in
    # for the cool folks running this script from an SSH-session or something
    print("♟️  Setting the right display...")
    os.environ["DISPLAY"] = ":0"

    print("♟️  Checking dependencies...")
    pkg = NPMPackage(os.path.realpath(
        f'{os.path.dirname(__file__)}/frontend/package.json'))
    
    # Install NPM packages
    pkg.install()
    
    # Execute electron using pynpm
    print("♟️  Starting frontend...")
    pkg.start(wait=False)

    # Initiate connection with the frontend
    frontendConnection = client.ServerProxy("http://localhost:9090")
    print("♟️  Pinging the frontend...")
    
    # Wait until RPC-server is reachable
    connectedToFrontend = False
    while connectedToFrontend == False:
        try:
            if frontendConnection.ping() == "pong":
                print("✔️  Succesfully connected to the frontend!")
                connectedToFrontend = True

        except:
            # If the server is not reachable yet, just wait a little bit and try again
            connectedToFrontend = False
            time.sleep(0.1)

    main()

initializeFrontend()
