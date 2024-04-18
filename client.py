from socket import * # type: ignore

#config
IP='127.0.0.1'
PORT=8080
BUFLEN=1024

#create an socket instance
data_socket=socket(AF_INET,SOCK_STREAM)
#bind socket to IP and PORT
data_socket.connect((IP,PORT))
print(f'connection established with {PORT} port')  

while True:
    #compile received message
    data=input('from me: ').encode()
    data_socket.send(data)
    recv=data_socket.recv(BUFLEN)
    recv=recv.decode()
    print('from server: ',recv)
    if recv=='':
        print(f'Closing the connection of {addr}') # type: ignore
        break
data_socket.close() 