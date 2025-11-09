import socket
import threading
import sys

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception:
        return "127.0.0.1"

def receive_messages():
    while True:
        try:
            message = clientSocket.recv(1024)
            if message:
                sys.stdout.write(f"\r{message.decode()}\n")
                sys.stdout.write("pesan : ")
                sys.stdout.flush()
        except:
            break

clientSocket = socket.socket()
client_ip = get_local_ip()
print(f'Alamat IP Client: {client_ip}')
server_host = input('Masukkan alamat IP Server: ')
server_port = int(input('Masukkan Port Server: '))
name = input('Masukkan username: ')
clientSocket.connect((server_host, server_port))

clientSocket.send(name.encode())
server_name = clientSocket.recv(1024)
server_name = server_name.decode()

print(server_name,' Telah bergabung...')

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

print("pesan : ", end="", flush=True)
while True:
    try:
        message = input()
        if message:
            clientSocket.send(message.encode())
        print("pesan : ", end="", flush=True)
    except:
        break