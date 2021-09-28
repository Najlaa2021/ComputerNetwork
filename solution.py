# import socket module
from socket import *
# In order to terminate the program
import sys
def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM) #OPEN SOCKET
    # Prepare a server socket
    serverSocket.bind(('127.0.0.1', port)) #BIND IT TO PORT NUMBER
    # Fill in start
    serverSocket.listen(5) # LISTNING AND WAITING
    # Fill in end
    while True:
        # Establish the connection
        print('openning accept...')
        print('Serving @ 127.0.0.1:{}'.format(port))
        connectionSocket, addr = serverSocket.accept() #ACCEPTING THE INCOMING CLIENT REQUEST
        print('Ready to serve...')
        try:
            try:
                message = connectionSocket.recv(1024).decode() # Fill in start    #Fill in end
                filename = message.split()[1]
                f = open(filename[1:])
                print("Serving Client: {}".format(filename))
                outputdata = f.readlines()
                f.close()
                # Fill in start     #Fill in end
                # Send one HTTP header line into socket.
                # Fill in start
                response = "HTTP/1.1 200 OK\r\n\r\n"
                print(response)
                connectionSocket.send(response.encode("utf-8"))
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode("utf-8"))
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                #Send response message for file not found (404)
                # Fill in start
                errorNotFound = "HTTP/1.1 404 Not Found\r\n\r\n"
                connectionSocket.send(errorNotFound.encode("utf-8"))
                print(errorNotFound)
        # Fill in end
        # Close client socket
        # Fill in start
            connectionSocket.close()
        # Fill in end
        except(ConnectionResetError, BrokenPipeError):
            pass
        serverSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)