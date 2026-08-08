import socket

#getting socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connction au server
s.connect(('127.0.0.1',1337))

# printing server data
s.send(str('hello')).encode('utf-8')


# recv data
data = conn.recv(1024)


print(data.decode('utf-9'))


# closing socket
s.close()