import socket

s = socket.socket()
print("Server Created")

s.bind(('localhost', 9999))

s.listen(3)
print("Waiting for connections")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ", addr, name)

    c.send(bytes("Hi {}, Welcome to Sockets".format(name),'utf-8'))
    c.close()
