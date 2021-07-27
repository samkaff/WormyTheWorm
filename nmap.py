#! /usr/bin/env python3

import nmap

nmScan = nmap.PortScanner()
nmScan.scan('10.0.0.94', '22')
nmScan.command_line()
for host in nmScan.all_hosts():
    print(host) 
    for proto in nmScan[host].all_protocols():
        lport = nmScan[host][proto].keys()
        for port in lport:
            print (port)
            print(nmScan[host][proto][port]['state'])


