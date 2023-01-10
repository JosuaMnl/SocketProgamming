import socket
import json
import rsa

# Server
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# Membuat Socket UDP
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

# Melakukan Binding Socket
sock.bind((UDP_IP, UDP_PORT))

# Decrypt
publicKey, privateKey = rsa.newkeys(512)


print("Menunggu Kiriman Pesan")

while True:
    data, addr = sock.recvfrom(1024)
    # y = json.loads(data.decode())
    decMsg = rsa.decrypt(data, privateKey).decode()
    y = json.loads(decMsg)

    print(addr)
    print(f"Dari User \t: {y['user']}")
    print(f"Pesan Diterima \t: {y['pesan']}")
    print(f"Waktu \t\t: {y['waktu']}")
