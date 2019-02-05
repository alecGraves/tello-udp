import socket
UDP_IP = "192.168.10.1"
UDP_PORT = 8889

print("Tello UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)


class Tello(object):
    def __init__(self, interface=2, timeout=2):
        self.sock = socket.socket(socket.AF_INET, # Internet
               socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
        # self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, interface)
        
        # set timeout in seconds
        self.sock.settimeout(timeout)

    def send(self, message, verbose=False):
        ret = self.sock.sendto(bytes(message, 'utf-8'), (UDP_IP, UDP_PORT))
        if verbose:
            print('sent', '"'+message+'"')
            print('waiting for response...')

        # Get return data:
        try:
            data, server = self.sock.recvfrom(UDP_PORT)
            if verbose:
                print('recieved', data, server)
            return data
        except socket.timeout:
            # Tello did not respond to command
            if verbose:
                print('timeout, recieved no data.')
            return "timeout"


if __name__ == "__main__":
    test = Tello()
    test.send("command")
    #test.send("time?")
    while True:
        test.send(input(">>>"), verbose=True)
