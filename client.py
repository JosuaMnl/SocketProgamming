import socket
import json
import rsa
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

pesan = input("Masukkan Pesan Anda \t: ")

print(f"Target IP \t\t: {UDP_IP}")
print(f"Target Port \t\t: {UDP_PORT}")
# print(f"Pesan \t\t\t: {pesan}")

# Membuat Socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
msg = {
    "user" : "Josua",
    "pesan" : pesan, 
    "waktu"  : current_time
    }
    
x = "Halooo"

publicKey, privateKey = rsa.newkeys(512)

encMsg = rsa.encrypt(x.encode(), publicKey)
print(f"Pesan \t\t\t: {encMsg}")
# Mengirim pesan ke server
sock.sendto(encMsg, (UDP_IP, UDP_PORT))                    