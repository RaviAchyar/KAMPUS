import socket
import threading
from datetime import datetime

# Alamat dan port server
host = '127.0.0.1'
port = 55555

# Inisialisasi socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Fungsi untuk mengirim pesan ke semua client
def broadcast(message):
    for client in clients:
        client.send(message)

# Fungsi untuk menangani pesan dari masing-masing client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break

            # Saat menerima pesan, server menambahkan waktu
            waktu = datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")
            broadcast(waktu.encode('ascii') + b" " + message)

        except:
            # Jika client keluar, hapus dari daftar
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} keluar!".encode('ascii'))
            nicknames.remove(nickname)
            break

# Fungsi utama untuk menerima koneksi client baru
def receive():
    print("Server berjalan dan menunggu koneksi...")
    tanggal = datetime.now().strftime("%A, %d %B %Y")
    print("Tanggal:", tanggal)

    while True:
        client, address = server.accept()
        print(f"Terhubung dengan {address}")

        # Kirim sinyal ke client untuk meminta nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')

        # Simpan client dan nickname-nya
        nicknames.append(nickname)
        clients.append(client)

        print(f"Username: {nickname}")
        broadcast(f"{nickname} bergabung ke chat!".encode('ascii'))
        client.send(f"Terkoneksi dengan server pada {tanggal}".encode('ascii'))

        # Jalankan thread untuk menangani pesan client ini
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
