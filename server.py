#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年12月24日
@author: william

'''

import socket

HOST=''
PORT=50007
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)



while 1:
    conn,addr=s.accept()
    print'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data:break
        print "data from: ", addr, data
        conn.sendall(data)
conn.close()