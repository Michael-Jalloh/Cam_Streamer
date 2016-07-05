from socket import *
import cv2
import numpy
from getpass import getpass

n = 25

def recvall(conn, count):
    buf = b''
    while count:
        newbuf = conn.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)

    return buf

try:
    sock = socket() # Create a socket object
    print 'Hello'
    ip = raw_input('Enter IP address of server: ')
    port = input('Enter Port number of server: ')
    print '==' * n
    sock.connect((ip, port))
    

    data = sock.recv(1024)
    print data
    ID = raw_input('Enter your ID: ')
    passd = getpass('Enter yur password: ')

    print '==' * n
    
    sock.send(ID+':'+passd)

    data = sock.recv(1024)
    if data == 'Denied':
        print 'Access Denied...'
        exit()

    while 1:
        length = recvall(sock, 16)
        if length == None:
            break
        
        buf = recvall(sock, int(length))
        data = numpy.fromstring(buf, dtype='uint8')

        decimg = cv2.imdecode(data, 1)
        cv2.imshow('Client', decimg)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sock.send('Quit')
            break
        else:
            sock.send('OK')

    sock.close()
    cv2.destroyAllWindows()
    
except:
    pass

exit(1)
