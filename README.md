# Cam_Streamer

These are a group of small python scripts use to stream video over a LAN.

## Usage

### Server
Inorder to use the server program there are some python module you will need to installed. 
open a terminal and install these modules

sudo apt-get install python-dev python-numpy python-opencv

sudo pip install peewee

please remember we are using opencv 2 not opencv 3.

There is one more module needed which is netifaces. You need to go to the page on python pypi website. Go to this [link](https://pypi.python.org/pypi/netifaces/#downloads), look for the source file at the download section. It should end with tar.gz

You will see how to install the package on the page.

RUNNING THE SERVER
Navigate to the Server folder
Before running the server your need to first create and account. So first run the manager.py program.

python manager.py 

follow the instructions to add a new user to your database. Without the users you wouldn't be able to logging on to the server.

enter 'quit' when you are done to close. now run the server program. 

python server.py

RUNNING THE CLIENT
Navigate to the Client folder
Before running the client program, make sure that you have install opencv, numpy 

run it by

python client.py

Conclusion
==========
Still got some work to do. Might add encryption


