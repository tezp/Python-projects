import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((socket.gethostbyname("127.0.0.1"),1133))
while True:
    sock.listen(5)
    (client,(ip,port)) = sock.accept()
    dataFromClient = client.recv(1024)
    print(dataFromClient.decode())
    msg = "Hiii "+dataFromClient.decode()
    client.send(msg.encode())
