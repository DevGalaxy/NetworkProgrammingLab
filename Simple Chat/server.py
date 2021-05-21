from socket import *
s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7898
s.bind((host,port))
s.listen(5)
print("listening")
c,ad=s.accept()
print("connection from",ad[0])
while True:
 x=c.recv(2048)
 print("client",x.decode("utf_8"))
 c.send(input("server:").encode("utf_8"))
c.close
s.close