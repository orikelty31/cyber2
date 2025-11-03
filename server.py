"""
Author: Ori Kelty
Program name: server.py
Description:
    This program is a TCP server that listens for client requests
    and responds based on a 4-character command.

    Supported commands:
    TIME - returns the current server time.
    NAME - returns the server name.
    RAND - returns a random number between 1 and 10.
    The server runs continuously and handles one client at a time.
    When a client sends the EXIT command, the server disconnects from the client and is ready to connecct with another client.

Date: 1/11/2025
"""

import socket
import datetime
import random
import logging

MAX_PACKET = 1024
SERVER_NAME = "Ori Server"
QUEUE_LEN = 1

def main():
    """
    Main function to start and run the TCP server.
    Waits for incoming client connections and handles each one.
    """
    while True:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            my_socket.bind(('0.0.0.0', 1729))
            my_socket.listen(QUEUE_LEN)
            client_socket, client_address = my_socket.accept()
            try :
                request = client_socket.recv(MAX_PACKET).decode()
                print('server received ' + request)
            except socket.error as err:
                print('received socket error on client socket' + str(err))
            finally:
                mode = client_socket.recv(MAX_PACKET).decode()
                if(mode == "TIME"):
                    logging.info("Client Requested Server Time")
                    client_socket.send(f"Current date and time: {Time()}".encode())
                elif(mode == "NAME"):
                    logging.info("Client Requested Server Name")
                    client_socket.send(('The Server Name Is: ' + Name()).encode())
                elif(mode == "RAND"):
                    logging.info("Client Requested A Random Number From 1-10")
                    client_socket.send(('The Random Number Is: ' + RandomNum()).encode())
                elif(mode == "EXIT"):
                    logging.info("The Client Disconnected")
                else:
                    logging.warning("The Client Didn't Want Nothing")
                    print("Warning Check server.log File")
                client_socket.close()
        except socket.error as err:
            print('received socket error on server socket' + str(err))
        finally:
            my_socket.close()

def Time():
    """
    Function that return current date and time.
    """
    time = datetime.datetime.now()
    return time


def Name():
    """
    Funcction that returns the name of the server.
    """
    return SERVER_NAME


def RandomNum():
    """
    Funtion that gives you a random number between 1 to 10.
    """
    return str(random.randint(1,10))


if __name__ == '__main__':
    logging.basicConfig(
        filename="server.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a",
    )


    assert Name() == "Ori Server" , "Assert Test Failed"
    assert 1 <= int(RandomNum()) <= 10, "Assert Test Failed"
    logging.info("All Assert Tests Passed")

    main()