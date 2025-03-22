#!/usr/bin/python3
from ssl import SOL_SOCKET
import select
from _socket import SO_REUSEADDR, SOCK_DGRAM, socket
# Local
from simple_dhcp_server.decoders import ReadBootProtocolPacket


def main():
    """Listen to DHCP traffic on the network."""
    s1 = socket(type = SOCK_DGRAM)
    s1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s1.bind(('', 67))
    #s2 = socket(type = SOCK_DGRAM)
    #s2.setsockopt(SOL_IP, SO_REUSEADDR, 1)
    #s2.bind(('', 68))
    while 1:
        reads = select.select([s1], [], [], 1)[0]
        for s in reads:
            packet = ReadBootProtocolPacket(*s.recvfrom(4096))
            print(packet)

if __name__ == '__main__':
    main()