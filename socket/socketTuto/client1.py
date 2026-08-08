import socket


host ,port = ("localhost",5055)

try :
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    print("un client vient de se connecter")

    #s.send(str("hi je suis le client")).encode()#methode1 pour znvoyer
    data = "hello im the clien: "
    data.encode("utf8")
    s.sendall(data)

except :
    print("Erreur de connexion\n")
finally:
    s.close()
