import  socket

mySocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mySocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
mySocket.connect(("127.0.0.1",1133))
mySocket.sendto("Tej".encode(),("127.0.0.1",1133))
data = mySocket.recvfrom(1248)
print(data[0])
