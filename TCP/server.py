import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print(f"Socket mendengar di alamat {TCP_IP} : {TCP_PORT}")

while True:
    conn, addr = s.accept()
    print(f"Mendengar koneksi dari {addr}")
    data = conn.recv(BUFFER_SIZE)
    print(f"Pesan diterima : {data.decode()}")

    pesan = "Hi" + str(addr)
    conn.send(pesan.encode())
    conn.close()