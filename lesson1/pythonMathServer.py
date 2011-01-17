#!/usr/bin/python

"""
Simple server that accepts takes 2 numbers and
replies with their sum. Demo of using sockets
"""

import socket

host = ''
port = 5008
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    dataList=data.split()
    result=int(dataList[0]) + int(dataList[1])
    result = str(result) 
    if data:
        client.send(result)
    client.close() 

