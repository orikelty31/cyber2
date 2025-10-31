import socket
import logging

MAX_PACKET = 1024
def main():
    option = None
    while(option != "EXIT"):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            my_socket.connect(('127.0.0.1', 1729))
            my_socket.send('Hello There'.encode())
        except socket.error as err:
            print('received socket error ' + str(err))
            logging.error("Could Not Connect To The Server")
        finally:
            logging.info("Successfully Connected To The Server")
            print("Hello Welcome To Our Server Please Choose One Of The Four Options You Can Choose")
            print("You Have TIME / NAME / RAND / EXIT")
            option = input("Please Choose One Of The Options: ").upper()
            opt_check = isinputvalid(option)
            if(opt_check == True):
                logging.info("The Client Chose : " +option)
                my_socket.send(option.encode())
            elif(opt_check == "EXIT"):
                my_socket.send(option.encode())
                logging.info("The Client Disconnected")
            else:
                while(opt_check == False):
                    logging.warning("The Client Didn't Choose One Of The Options")
                    print("Please Choose One Of The Options")
                    print("You Have TIME / NAME / RAND / EXIT")
                    option = input("Please Choose One Of The Options: ").upper()
                    opt_check = isinputvalid(option)
                    if(option == ""):
                        while(not option):
                            logging.warning("The Client Didn't Write Anything")
                            print("Please Write Something")
                            option = input("Please Choose One Of The Options: ").upper()
                            opt_check = isinputvalid(option)

                logging.info("The Client Chose : " + option)
                my_socket.send(option.encode())
            response = my_socket.recv(MAX_PACKET).decode()
            print(response)
            my_socket.close()

def isinputvalid(option):
    if(option == "TIME" or option == "NAME" or option == "RAND"):
        return True
    elif(option == "EXIT"):
        return "EXIT"
    else:
        return False

if __name__ == '__main__':
    logging.basicConfig(
        filename="client.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a",
    )


    assert isinputvalid("TIME") == True , "Assert Test Failed"
    assert isinputvalid("BLABLA") == False , "Assert Test Failed"
    assert isinputvalid("EXIT") == "EXIT" , "Assert Test Failed"
    logging.info("All Assert Tests Passed")
    main()