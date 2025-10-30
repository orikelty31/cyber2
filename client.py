import socket

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
        finally:
            print("Hello Welcome To Our Server Please Choose One Of The Four Options You Can Choose")
            print("You Have TIME / NAME / RAND / EXIT")
            option = input("Please Choose One Of The Options: ").upper()
            if(option):
                my_socket.send(option.encode())
            else:
                while(not option):
                    print("Please Write Something")
                    option = input("Please Choose One Of The Options: ").upper()
                    my_socket.send(option.encode())
            response = my_socket.recv(MAX_PACKET).decode()
            print(response)
            my_socket.close()

if __name__ == '__main__':
    main()