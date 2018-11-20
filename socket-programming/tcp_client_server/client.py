import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostbyname("127.0.0.1"), 1133))
while True:
    sock.send("Tejprakash".encode())
    print(sock.recv(1024).decode())

