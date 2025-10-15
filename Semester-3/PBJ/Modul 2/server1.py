import socket
import threading
import time

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.bind(("127.0.0.1", 12345))
print("Server menunggu...")

nomer = 0
lock = threading.Lock()  # untuk keamanan akses variabel di multi-thread

def func(number):
    x = socketClient.recvfrom(1024)
    addrs = x[1][0]
    msg = x[0].decode()
    no = str(number)
    print("User-" + no + " : " + msg)
    try:
        time.sleep(int(msg))
    except ValueError:
        pass
    print("User-" + no + " : " + msg)

while True:
    with lock:
        nomer += 1
        t = threading.Thread(target=func, args=(nomer,))
        t.start()
