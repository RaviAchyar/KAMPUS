import socket
import threading
import sys
from datetime import datetime

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 5001))

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

def receive_messages():
    while True:
        try:
            message = msg.recv(1024)
            if message:
                message = message.decode()
                current_time = datetime.now().strftime("%H:%M:%S")
                sys.stdout.write(f"\r[{current_time}] {client}: {message}\n")
                sys.stdout.write(f"[{name}] pesan: ")
                sys.stdout.flush()
        except:
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

print(f"[{name}] pesan: ", end="", flush=True)
while True:
    try:
        server_message = input()
        if server_message:
            current_time = datetime.now().strftime("%H:%M:%S")
            timestamped_message = f"[{current_time}] {name}: {server_message}"
            msg.send(timestamped_message.encode())
        print(f"[{name}] pesan: ", end="", flush=True)
    except:
        break