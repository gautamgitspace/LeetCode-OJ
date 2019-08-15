#!/usr/bin/env python
import re

def defang(ip_addr):
    if '.' in ip_addr:
        return ip_addr.replace('.', '[.]')

if __name__ == "__main__":
    ip_addr = '192.168.10.5'
    print defang(ip_addr)
