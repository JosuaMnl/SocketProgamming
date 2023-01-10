import socket
import json

# Server
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# Membuat Socket UDP
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

# Melakukan Binding Socket
sock.bind((UDP_IP, UDP_PORT))

print("Menunggu Kiriman Pesan")

while True:
    data, addr = sock.recvfrom(1024)
    y = json.loads(data)

    print(addr)
    print(f"Dari User \t: {y['user']}")
    print(f"Pesan Diterima \t: {y['pesan']}")
    print(f"Waktu \t\t: {y['waktu']}")
