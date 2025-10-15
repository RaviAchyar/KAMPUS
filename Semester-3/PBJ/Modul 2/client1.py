import socket

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.connect(("127.0.0.1", 12345))

while True:
    angka = input('Masukkan angka >> ')
    b = str.encode(angka)
    socketClient.send(b)
