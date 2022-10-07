import xmlrpc.client

def update(player, boardstate):

    # Create RPC connection with the frontend
    frontendConnection = xmlrpc.client.ServerProxy("http://localhost:9090")
    frontendConnection.update({"boardstate": boardstate, "player": player})
    return True