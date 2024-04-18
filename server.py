from socket import *

IP='127.0.0.1'
PORT=8080
BUFLEN=1024

#AF_INT:IP   SOCK_STREAM:TCP
listen_socket=socket(AF_INET,SOCK_STREAM)

listen_socket.bind((IP,PORT))
listen_socket.listen(5)
print(f'Server starts listening to {IP}:{PORT}...')

client_socket,addr=listen_socket.accept()
print(f' Server connect with {IP}:{PORT}...')

while True:
    rev=client_socket.recv(BUFLEN)
    print(f'from client: {rev}')
    client_socket.send(input('from me: ').encode())
    if not rev:
        print(f'Closing the connection of {addr}')
        break 
client_socket.close()
