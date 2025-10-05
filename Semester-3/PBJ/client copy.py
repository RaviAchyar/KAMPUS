import socket

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.connect(("127.0.0.1", 5002))

while True:
    a = input('message>> ')
    b = str.encode(a)
    socketClient.send(b)

    if a.lower() == "exit":  # tambahkan opsi keluar
        print("Client disconnected.")
        break
