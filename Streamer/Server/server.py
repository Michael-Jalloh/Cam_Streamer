from socket import *
import cv2
import numpy
import netifaces as ni
from models import *


def get_ip():
	interfaces = ['eth0','eth1','eth2','wlan0','wlan1','wlan2']
	for i in interfaces:
		try:
			ip = ni.ifaddresses(i)[2][0]['addr']
			return ip
		except:
			pass
	return None

sock = socket()
ip = get_ip()
if ip == None:
	print '[INFO] No network interface found'
	print '[INFO] Exiting...'
	exit()
	
	
sock.bind((ip,5000))
sock.listen(True)
print '[INFO] Server Started...'
print '[INFO] Listening on IP:{} Port:{}'.format(ip,5000)
sock.close()
print '[INFO] Closing Socket'
