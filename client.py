import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

pesan = input("Masukkan Pesan Anda \t: ")

print(f"Target IP \t\t: {UDP_IP}")
print(f"Target Port \t\t: {UDP_PORT}")
print(f"Pesan \t\t\t: {pesan}")

# Membuat Socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

# Mengirim pesan ke server
sock.sendto(pesan.encode(), (UDP_IP, UDP_PORT))                    