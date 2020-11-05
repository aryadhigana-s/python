import socket
import threading
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind(('192.168.137.1',8080))
s.listen(5)
# print("Waiting . . . .")
# conn, addr = s.accept()
# print(addr, "has connected")
#
# kata = input("Sapa lah dia: ")
# conn.send(kata)
#
# print("sended")


while True:
    conn, addr = s.accept()
    print(f"Connetion from {addr} has been established ")
    # kata = input("Sapa lah dia :")
    # conn.send(bytes(kata,"utf-8"))

    # kata = conn.recv(1024)
    fileSize = s.recv(1024)
    print(fileSize)
    s.send('OK')
    data = long(s.recv(1024))
    Print("Complete")


    #print(kata.decode("utf-8"))
    s.close()


