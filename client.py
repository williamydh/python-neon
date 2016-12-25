#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年12月24日

@author: william
'''


# Echo server program
import socket 
import time

HOST='192.168.3.71'
PORT=50007
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
    s.sendall('Hello World!')
    data=s.recv(1024)
    print'Received',repr(data)
    time.sleep(2)
s.close()