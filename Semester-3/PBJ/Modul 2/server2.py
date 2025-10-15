import socket
import threading
import time

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
nomer = 0
socketClient.bind(("127.0.0.1", 12345))
print("Server menunggu...")

def func(number):
    x = socketClient.recvfrom(1024)
    addrs = x[1][0]
    msg = x[0].decode()
    no = str(number)
    print("User-" + no + " : " + msg)

    try:
        waktu = int(msg)
        time.sleep(waktu)
        print("User-" + no + " : " + msg)
    except:
        pass

while True:
    nomer += 1
    t = threading.Thread(target=func, args=(nomer,))
    t.start()
