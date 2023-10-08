#!/usr/bin/env python
import socket
import psutil
import subprocess
amarillo = '\033[93m'
rojo = '\033[91m'
resetColor = '\033[0m'
verde = '\033[92m'

def obtener_ip():
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except Exception as e:
        return str(e)

def obtener_mac():
    try:
        interfaces = psutil.net_if_addrs()
        mac_addresses = {}
        for interface, addrs in interfaces.items():
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    mac_addresses[interface] = addr.address
        return mac_addresses
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    ip = obtener_ip()
    macs = obtener_mac()
    print(amarillo+f"\nTu dirección IP es: {ip}\n"+resetColor)
    print(verde+"[----> Direcciones MAC <----]"+resetColor)
    for interface, mac in macs.items():
        print(amarillo+"\n=> ["+resetColor+verde+f"{interface}:"+resetColor+amarillo+f"{mac}"+resetColor+amarillo+"] <="+resetColor)
