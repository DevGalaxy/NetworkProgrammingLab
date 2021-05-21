from socket import *
from _thread import *
import threading

s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000

def recieved_thread(c):
    while True:
        x = c.recv(2000)
        print(x.decode("utf=8"))
        
s.connect((host, port))
start_new_thread(recieved_thread, (s,))

while True:
    s.send(input("client>> ").encode("utf=8"))


