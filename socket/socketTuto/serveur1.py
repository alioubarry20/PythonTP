import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host , port =("",5055)
s.bind(("host",5055))


while True:
    s.listen(10)
    conn ,addr = s.accept()
    print("un client vient de se connecter")
    data = conn.recv(1024).decode('utf8')
    print(data)
    


conn.close()
s.close()


