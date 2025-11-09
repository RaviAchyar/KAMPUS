import socket

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception:
        return "127.0.0.1"

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
while True:
    message = input("pesan : ")
    clientSocket.send(message.encode()) 