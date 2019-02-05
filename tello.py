import socket
UDP_IP = "192.168.10.1"
UDP_PORT = 8889

print("Tello UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)


class Tello(object):
    def __init__(self, interface=2):
        self.sock = socket.socket(socket.AF_INET, # Internet
               socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
        # self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, interface)
        self.sock.settimeout(2)
    def send(self, message):
        ret = self.sock.sendto(bytes(message, 'utf-8'), (UDP_IP, UDP_PORT))
        print('sent', '"'+message+'"')
        print('waiting for response...')
        try:
            data, server = self.sock.recvfrom(UDP_PORT)
            print('recieved', data, server)
        except socket.timeout:
            print('timeout, recieved no data.')


if __name__ == "__main__":
    test = Tello()
    test.send("command")
    #test.send("time?")
    while True:
        test.send(input(">>>"))
