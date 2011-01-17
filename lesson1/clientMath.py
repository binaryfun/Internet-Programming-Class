#!/usr/bin/python
# Echo client program
import socket
import sys

if len(sys.argv) != 3:  # the program name and the two arguments
  # stop the program and print an error message
  sys.exit("Must provide two positive numbers\n \
  Example: %s 123 1213" % sys.argv[0] )

# Convert the two arguments from strings into numbers
x =sys.argv[1]
y =sys.argv[2]


HOST = ''    # The remote host
PORT = 5008             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
fullTextToSend = "%s %s" % (x,y)
s.send(fullTextToSend)
data = s.recv(1024)
s.close()
print 'Received', repr(data)

