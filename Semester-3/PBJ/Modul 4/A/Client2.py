import socket
import threading

userName = input("Masukkan username: ")

# Membuat koneksi ke server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = input("Masukkan IP Server: ")
server_port = int(input("Masukkan Port Server: "))
client.connect((server_host, server_port))

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

def write():
    while True:
        try:
            message = f'{userName}: {input(">> ")}'
            client.send(message.encode('ascii'))
        except:
            print("Koneksi ditutup.")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
