import socket, threading, time, random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("127.0.0.1", 12345))

user = input("Masukkan username >> ")

kata_list = ["halo", "hai", "hola", "hello", "annyeong", "ciao", "salut"]
kata_user = random.choice(kata_list)

def kirim_otomatis():
    while True:
        sock.send(f"{user}: {kata_user}".encode())
        time.sleep(1)

def kirim_manual():
    while True:
        msg = input("Pesan >> ")
        if msg.lower() in ["exit", "keluar", "quit"]:
            print("Menutup client...")
            sock.close()
            exit()
        sock.send(f"{user}: {msg}".encode())

threading.Thread(target=kirim_otomatis, daemon=True).start()
kirim_manual()
