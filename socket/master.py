from socket import *

master = socket(AF_INET, SOCK_STREAM)
master.bind(("127.0.0.1", 80))
master.listen(1)
con, addr = master.accept()
con.send("Hi".encode("utf-8"))
print(con.recv(1024).decode("utf-8"))