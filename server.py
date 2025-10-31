import socket
import datetime
import random
import logging

MAX_PACKET = 1024
SERVER_NAME = "Ori Server"
QUEUE_LEN = 1

def main():
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
    time = datetime.datetime.now()
    return time

def Name():
    return SERVER_NAME

def RandomNum():
    return str(random.randint(1,10))


if __name__ == '__main__':
    logging.basicConfig(
        filename="server.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a",
    )
    """"
    # Test messages
    logger.debug("Harmless debug Message")
    logger.info("Just an information")
    logger.warning("Its a Warning")
    logger.error("Did you try to divide by zero")
    logger.critical("Internet is down")
    """
    main()