from socket import *
from _thread import *
import threading

def receive_thread(s):
 while True:
  x=s.recv(2000)
  print("server:",x.decode('utf_8'))

s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7898
s.connect((host,port))
start_new_thread(receive_thread,(s,))
while True:
 d=input()
 s.send(d.encode('utf_8'))