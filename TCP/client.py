import socket

TCP_IP = "192.168.3.123"
TCP_PORT = 5005
BUFFER_SIZE = 1024
pesan = input("Masukkan Pesan Anda : ")

s = socket.socket(socket.AF_INET, \
    socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))
s.send(pesan.encode())
data = s.recv(BUFFER_SIZE)
s.close()

print(f"Pesan diterima {data.decode()}")