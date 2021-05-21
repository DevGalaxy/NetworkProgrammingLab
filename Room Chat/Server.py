from socket import *
from _thread import *
import threading

s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.bind((host, port))
s.listen(5)
clients = [] 

def connect_new_user(sessionId, socketInfo):
    print(socketInfo[0] + " is now connected.")
    while True:
        message = sessionId.recv(2000)
        message = socketInfo[0] + ':' + message.decode('utf=8')
        send_to_all(message, sessionId)


def send_to_all(message, sessionId):
    for client in clients:
        if client != sessionId:
            client.send(message.encode("utf=8"))

while True:
    sessionId, socketInfo = s.accept()
    clients.append(sessionId)
    start_new_thread(connect_new_user, (sessionId, socketInfo))
session.close()

