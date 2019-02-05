import socket
import sys
import cv2

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port

# state info messages
# server_address = ('0.0.0.0', 8890)

# state info messages
server_address = ('0.0.0.0', 11111)
sock.bind(server_address)

video = ''

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received %s bytes from %s' % (len(data), address))
    print (data)

    if data:
        pass
        #sent = sock.sendto(data, address)
        #print('sent %s bytes back to %s' % (sent, address))
