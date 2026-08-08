import socket

# creation du socekt
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#ipv4 et tcp
s.bind(('127.0.0.1',1337))

#listenning 
s.listen()
# getting client
conn,addr = s.accept()
print("new connxion by",addr)

# revice
data = s.recv(1024)
print(data.decode('utf-8'))
#reading to client
if data.decode('utf-8') == 'hello':
    conn.send(str('[server]: hi !')).encode('utf-8')


#fermer la connexion
conn.close()
s.close()

