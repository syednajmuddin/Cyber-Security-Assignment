import socket
c = socket.socket()
c.connect(("127.0.0.1", 5000))
while True:
    msg = input("You: ")
    if msg == "exit": break
    c.send(msg.encode())
    print(c.recv(1024).decode())
c.close()