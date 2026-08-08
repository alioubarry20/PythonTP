import socket

#session UDP
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# permet de libere le port/client apres utilisation
addrPort = ("127.0.0.1", 3000)

client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.sendto(b"Hello from client", addrPort)

msg=client.recv(1024).decode('utf-8')
print("MEssage du serveur:",msg)

client.close()