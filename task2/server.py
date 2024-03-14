import socket
import threading

HOST = '127.0.0.1'  # Стандартный адрес интерфейса обратной петли (localhost)
PORT = 8080 


def handle_client(client_socket, address):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        decoded_data = data.decode('utf-8')
        response = decoded_data.upper()
        client_socket.sendall(response.encode('utf-8'))
    client_socket.close()
    

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        while True:
            client_socket, address = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()
    except KeyboardInterrupt:
        print('Сервер остановлен')
        server.close()

if __name__ == '__main__':
    start_server()