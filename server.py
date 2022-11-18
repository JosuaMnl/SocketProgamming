import socket

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
    print(addr)
    print(f"Pesan Diterima \t: {data.decode()}")
