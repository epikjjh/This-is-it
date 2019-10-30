from socket import *
import threading
import time

def send(sock):
    while True:
        data = input()
        sock.send(data.encode("utf-8"))
    sock.close()
    
def receive(sock):
    while True:
        data = sock.recv(1024).decode("utf-8")
        print(data)
    sock.close()
slave = socket(AF_INET, SOCK_STREAM)
slave.connect(("127.0.0.1", 80))
sender = threading.Thread(target=send, args=(slave,))
receiver = threading.Thread(target=receive, args=(slave,))
sender.start()
receiver.start()
while True:
    time.sleep(1)
    pass