import socket
import threading
from datetime import datetime

# Input data dari pengguna
userName = input("Masukkan username: ")
server_host = input("Masukkan IP Server: ")
server_port = int(input("Masukkan Port Server: "))

# Membuat koneksi ke server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_host, server_port))

# Fungsi untuk menerima pesan dari server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(userName.encode('ascii'))
            else:
                print(message)
        except:
            print("Terjadi kesalahan atau koneksi terputus!")
            client.close()
            break

# Fungsi untuk mengirim pesan ke server
def write():
    while True:
        try:
            teks = input(">> ")
            waktu = datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")
            message = f"{waktu} {userName}: {teks}"
            client.send(message.encode('ascii'))
        except:
            print("Koneksi ditutup.")
            client.close()
            break

# Menjalankan dua thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
