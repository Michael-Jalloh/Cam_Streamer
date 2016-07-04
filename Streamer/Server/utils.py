# import the necessary modules
from threading import Thread
import cv2 
from models import *
import netifaces as ni
import numpy


class Cam:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.encode_params = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        self.frame = None
        
        # initiaize the variable needed to stop the thread
        self.stopped  = False
        
    def start(self):
        # Start the thread to read frames from the cam
        Thread(target=self.update, args=()).start()
        return self
        
    def update(self):
        # Keep looping infinitely until thread is stopped
        ret, frame = self.stream.read()
        while not ret:
            if self.stopped:
                break
            ret, frame = self.stream.read()
            
        while True:
            # if the thread stop variable is set, stop the thread
            if self.stopped:
                self.stream.release()
                
            # Else
            self.grabbed, self.frame = self.stream.read()
            
    def read(self):
        # Return th capture frame
        return self.frame
        
    def stop(self):
        # set the thread stop variable
        self.stopped = True 
        
    def stringData(self):
        result, imgencode = cv2.imencode('.jpg', self.frame, self.encode_params)
        data = numpy.array(imgencode)
        return data.tostring()


class Client:
    def __init__(self, conn, cam):
                
        self.conn = conn # pass in the socket connection
        self.cam = cam # pass in the camera object
        self.stopped = False # Set the stop variable for the thread to False
                
    def start(self):
        # Start the sending thread
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
                if self.stopped:
                        break
                data = self.cam.stringData()
                self.conn.send(str(len(data)).ljust(16))
                self.conn.send(data)

                reply = self.conn.recv(1024)
                if reply== 'Quit':
                        self.stop()

        #self.conn.send('quit')
        self.conn.close()

    def stop(self):
        # stop the thread
        self.stopped = False

                
                
def check_user(data):
    try:
        ID, passd = data.split(':')
        ID = int(ID)
        user = User.get(id = ID)
        if user.verify_password(passd):
            return True
        else:
            return False
            
    except:
        return False
    
    
    
def get_ip():
        interfaces = ['wlan0','wlan1','eth0','eth1','lo']
        for i in interfaces:
                print i
                try:
                        ip = ni.ifaddresses(i)[2][0]['addr']
                        return ip
                except:
                        pass
        return None
        
    
                        
                
