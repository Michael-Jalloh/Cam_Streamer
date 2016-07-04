from socket import *
import cv2
import numpy
import netifaces as ni
from models import *
from utils import *



n = 25
cam = Cam()
cam.start()

sock = socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ip = get_ip() 
print ip
if ip == None:
	print '[INFO] No network interface found'
	print '[INFO] Exiting...'
	print '==' * n
	exit()
	
	
sock.bind((ip,5000))
sock.listen(True)
print '[INFO] Server Started...'
print '[INFO] Listening on IP:{} Port:{}'.format(ip,5000)
print '==' * n
while 1:
        conn,addr = sock.accept()
        print '[INFO] Client Connected from IP: {} Port: {}'.format(addr[0],addr[1])
        conn.send('Please Authenticate')
        data = conn.recv(1024)
        if check_user(data):
                print 'User authenticated....'
                print '==' * n
                conn.send('Authenticated')
                client  = Client(conn, cam)
                client.start()
        else:
                print '[INFO] User can\'t b authnticated...'
                print '[INFO] Closing connection...'
                print '==' * n
                conn.send('Denied')
                conn.close()

cam.stop()               
sock.close()
print '[INFO] Closing Socket'
