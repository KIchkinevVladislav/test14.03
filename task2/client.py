import socket

HOST = '127.0.0.1'
PORT = 8080

message = input('Пожалуйста, введите текст, который хотите передать: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024) 
    print(data.decode())