#!/usr/bin/python

from socket import *
import cv2
import numpy

def recvall(sock, count):
	buf = b''
	while count:
		newbuf = sock.recv(count)
		if not newbuf: return None
		buf += newbuf
		count -= len(newbuf)
	return buf


TCP_IP = raw_input('Enter your IP address: ')
TCP_PORT = raw_input('Enter the Port number: ')

if TCP_IP:
        pass
else:
        TCP_IP = 'localhost'
        
if TCP_PORT:
        TCP_PORT = int(TCP_PORT)
else:
        TCP_PORT = 5000

s = socket()
s.bind((TCP_IP, TCP_PORT))
s.listen(True)
print '[INFO] Server started on IP:{} port:{}'.format(TCP_IP, TCP_PORT)
print '[INFO] Waiting for client to connect'
conn, addr = s.accept()
print'[INFO] Client connected from IP:{}'.format(addr[0])

while 1:
        length = recvall(conn, 16)
        print length
        if length == None:
                break
        stringData = recvall(conn, int(length))
        data = numpy.fromstring(stringData,dtype='uint8')


        decimg = cv2.imdecode(data,1)
        cv2.imshow('Server',decimg)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
conn.close()
cv2.destroyAllWindows()
exit(1)
