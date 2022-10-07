import xmlrpc.client

def prompt(player, parameter):

    # Create RPC connection with the frontend
    frontendConnection = xmlrpc.client.ServerProxy("http://localhost:9090")
    answer = frontendConnection.prompt({"parameter": parameter, "player": player})["answer"]
    print(answer)
    # Get the data from the frontend and return it
    return answer
