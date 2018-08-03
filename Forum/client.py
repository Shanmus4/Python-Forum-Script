import socket
import threading

def send(uname):
    while True:
        msg = input('\n')
        data = uname + '>>>>>' + msg
        data=data.encode(encoding='UTF-8')                  #send data in an encoded format..
        cli_sock.sendall(data)                  

def receive():
    while True:
        data = cli_sock.recv(1024)
        print('\n'+ str(data.decode()))

if __name__ == "__main__":   
    
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  
    HOST = '192.168.43.82'
    PORT = 5023 #Can be any port, but same on server

    uname = input('Enter your name to enter the chat! > ')

    cli_sock.connect((HOST, PORT))     
    print('Connected to remote host...\n')


    thread_send = threading.Thread(target = send,args=[uname])
    thread_send.start()

    thread_receive = threading.Thread(target = receive)
    thread_receive.start()