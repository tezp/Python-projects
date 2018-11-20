import  socket

mySocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
mySocket.bind(("127.0.0.1",1133))
#mySocket.listen(5)
(msg, addr)=mySocket.recvfrom(1248)
print(msg,addr)
mySocket.sendto("Hii {}".format(msg.decode()).encode(),addr)
