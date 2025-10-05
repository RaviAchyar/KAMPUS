import socket
import time

# Input IP dan Port server secara dinamis
server_ip = input("Masukkan IP Address Server: ")
server_port = int(input("Masukkan Port Server: "))

# Buat socket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.connect((server_ip, server_port))

print("Ketik 'stop' untuk menghentikan pengiriman data.")

counter = 1
while True:
    pesan = f"pesan{counter}"
    socketClient.send(pesan.encode())
    print(f"Data terkirim: {pesan}")
    counter += 1

    # jeda sedikit biar tidak terlalu cepat
    time.sleep(1)

    # opsi menghentikan lewat input
    try:
        stop = input("Ketik 'stop' untuk berhenti atau tekan Enter untuk lanjut: ")
        if stop.lower() == "stop":
            print("Pengiriman data dihentikan.")
            break
    except KeyboardInterrupt:
        print("\nPengiriman dihentikan dengan Ctrl+C")
        break
