#!/usr/bin/python
from socket import *
import cv2
import numpy


TCP_IP = raw_input('Enter server IP address: ')
TCP_PORT = raw_input('Enter server listening port: ')

if TCP_IP:
    pass
else:
    TCP_IP='localhost'

if TCP_PORT:
    TCP_PORT = int(TCP_PORT)
else:
    TCP_PORT = 5000

sock = socket()

sock.connect((TCP_IP,TCP_PORT))
print '[INFO] Connected to server on IP:{} port:{}'.format(TCP_IP, TCP_PORT)

capture = cv2.VideoCapture(0)

while 1:
    ret, frame = capture.read()
    frame = cv2.flip(frame,1)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()

    sock.send(str(len(stringData)).ljust(16))
    sock.send(stringData)
    
    print ret
    cv2.imshow('Client', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.send('quit')
sock.close()
capture.release()
cv2.destroyAllWindows()
exit(1)
