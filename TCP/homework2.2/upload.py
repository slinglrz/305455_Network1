import sys
import socket 
import os

TCP_IP = "127.0.0.1"
TCP_PORT = 5005
FILE_NAME = 'test.png'

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "Pic:", FILE_NAME


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(10)

while 1:
    data,addr = sock.accept()
    new = r'upload/' 
    if not os.path.exists(new):
        os.makedirs(new)

    fileupload = open(new + FILE_NAME, "wb")
    data = data.recv(1024)
    while data:
        fileUpload.write(Data)
        data = data.recv(1024)
    print "Upload Finish"
sock.close()
