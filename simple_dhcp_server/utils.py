import socket

import psutil
from scapy.all import show_interfaces


def get_interfaces():
    ifaces = show_interfaces()
    print(ifaces)
    return ifaces


def get_interface_by_ip(ip_address):
    # Get all network interfaces
    addrs = psutil.net_if_addrs()

    # Iterate over the interfaces and check the associated IP address
    for iface, iface_info in addrs.items():
        for addr in iface_info:
            if addr.family == socket.AF_INET and addr.address == ip_address:
                return iface
    return None
