import socket

clientSocket = socket.socket()
print('Alamat IP Client: 127.0.0.1')
server_host = input('Masukkan alamat IP Server: ')
name = input('Masukkan username: ')
clientSocket.connect(("127.0.0.1", 12345))

clientSocket.send(name.encode())
server_name = clientSocket.recv(1024)
server_name = server_name.decode()

print(server_name,' Telah bergabung...')
while True:
    message = input("pesan : ")
    clientSocket.send(message.encode())