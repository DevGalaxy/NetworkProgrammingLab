from socket import *
from _thread import *
import threading

def receive_thread(sessionId):
 while True:
  data=sessionId.recv(2000)
  print("client:",data.decode('utf_8'))

def client_thread(sessionId):
 start_new_thread(receive_thread,(sessionId,))
 while True:
  sessionId.send(input().encode('utf_8'))

s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7898
s.bind((host,port))
s.listen(5)

print("listening")

while True:
 sessionId,socketInfo=s.accept()
 print("connection from",socketInfo[0])
 start_new_thread(client_thread,(sessionId,))
 