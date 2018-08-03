import socket
import threading

list=[]
y='\n'                                          #for next line while sending old content
y=y.encode(encoding='UTF-8')                       #encode '\n' character

def accept_client():
    while True:                                         #accepting new client
        cli_sock, cli_add = ser_sock.accept()
        CONNECTION_LIST.append(cli_sock)
        for i in list:
            cli_sock.send(i)
            cli_sock.send(y)                                #send new line character
            
        thread_client = threading.Thread(target = broadcast_usr, args=[cli_sock])
        thread_client.start()

def broadcast_usr(cli_sock):
    while True:
        try:
            flag=0
            data = cli_sock.recv(1024)
            list.append(data)                                   #append all data to a list so when a new user logs in all the old data will be displayed
            
            if data:
                b_usr(cli_sock, data)
        except Exception as x:
            print(x.message)
            break

def b_usr(cs_sock, msg):
    for client in CONNECTION_LIST:
        if client != cs_sock:
            client.send(msg)

if __name__ == "__main__":    
    CONNECTION_LIST = []

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = 'localhost'
    PORT = 5023
    ser_sock.bind((HOST, PORT))

    # listen    
    ser_sock.listen(1)
    print('Chat server started on port : ' + str(PORT))

    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()