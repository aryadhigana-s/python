import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.137.1',8080))

# conn, addr = s.accept()
# print('Connected with ',addr)

kata = input("Sapa lah dia :")
s.send(bytes(kata,"utf-8"))
# kata = s.recv(1024)
# print(kata.decode("utf-8"))