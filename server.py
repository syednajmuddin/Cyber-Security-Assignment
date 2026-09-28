import socket
s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen(1)
print("Waiting...")
conn, addr = s.accept()
print("Connected:", addr)
while True:
    data = conn.recv(1024)
    if not data: break
    print("Client:", data.decode())
    conn.send(b"Server got: " + data)
conn.close()