from socket import *
s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7898
s.connect((host,port))
while True:
 d=input("client:")
 s.send(d.encode("utf_8"))
 y=s.recv(2048)
 print("server:",y.decode("utf_8"))
s.close