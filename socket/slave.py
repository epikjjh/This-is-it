from socket import *

slave = socket(AF_INET, SOCK_STREAM)
slave.connect(("127.0.0.1", 80))
print(slave.recv(1024).decode("utf-8"))
slave.send("Bye".encode("utf-8"))