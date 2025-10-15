import socket
import time
import threading

stop_flag = False

def check_stop():
    global stop_flag
    while True:
        command = input()
        if command.lower() == "stop":
            stop_flag = True
            print("Perintah 'stop' diterima. Menghentikan pengiriman data...")
            break

server_ip = input("Masukkan IP Address Server: ")
server_port = int(input("Masukkan Port Server: "))

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.connect((server_ip, server_port))

print(f"\nTerhubung ke server {server_ip}:{server_port}")
print("Mulai mengirim data secara otomatis...")
print("Ketik 'stop' untuk menghentikan pengiriman.\n")

threading.Thread(target=check_stop, daemon=True).start()

counter = 1
while not stop_flag:
    pesan = f"pesan{counter}"
    socketClient.send(pesan.encode())
    print(f"Data terkirim: {pesan}")
    counter += 1
    time.sleep(1)

socketClient.close()
print("Pengiriman data dihentikan. Program selesai.")
