import socket
import json
from datetime import datetime

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

pesan = input("Masukkan Pesan Anda \t: ")

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
msg = {
    "user" : "Josua",
    "pesan" : pesan, 
    "waktu"  : current_time
}

x = json.dumps(msg)
print(f"Target IP \t\t: {UDP_IP}")
print(f"Target Port \t\t: {UDP_PORT}")
print(f"Pesan \t\t\t: {x.encode()}")

# Membuat Socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

# Mengirim pesan ke server
sock.sendto(x.encode(), (UDP_IP, UDP_PORT))                    