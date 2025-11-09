import socket
from datetime import datetime

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 12345))

print("Alamat IP: 127.0.0.1")
current_date = datetime.now().strftime("%d/%m/%Y")
print(f"Tanggal: {current_date}")
name = input('Masukkan Username: ')
serverSocket.listen()

msg, addrs = serverSocket.accept()
print("Menerima koneksi dari ", addrs[0])
print('Connection Established. Terkoneksi dari: ', addrs[0])

client = (msg.recv(1024)).decode()
print(client + ' sudah terhubung.')
msg.send(name.encode())

while True:
    message = msg.recv(1024)
    message = message.decode()
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] {client}: {message}")