# WormyTheWorm
___

### Summary: 
> A Python worm that scans & infects a given subnet. 
> Below is a breakdown of the code, including screenshots & descriptions of the processes used. 

### Table of Contents
- Dependents (imports - paramiko, nmap, scp)
- NMap (defining a subnet, why port 22, first for loop = host list)
- Brute Force (Defining wordlists - using own or rockyou etc)
- Paramiko (looping through usernames & passwords, connecting via ssh, executing bash)
- SSH
- Try / Except
- SCP (transfering file from host using GET)

## Dependents 
&NewLine;
```sh
import nmap
import paramiko
import sys
from scp import SCPClient
```
The above must be installed on the local machine for the program to run successfully. Use the below code to install each successfully. 

**Pip:**
```sh
sudo apt install python3-pip
```
**NMap:**
```sh
sudo apt-get install nmap
pip install python-nmap
```
**Paramiko:**
```sh
pip install paramiko
```
**SCP:**
```sh
pip install git+https://github.com/jbardin/scp.py
```
## NMap

NMap is used to scan a given subnet & return all host IPs on the network. 

**NMap Explained**

1. A variable is defined that calls the port scanner method. 
2. **The target subnet is identified - the default port will always be 22 for SSH utilization.**
3. The command line method is initialized. 
```sh
nmScan = nmap.PortScanner()
nmScan.scan('10.0.0.0/24', '22')
nmScan.command_line()
```
1. A list called "networkhosts" is defined, which will contain the IPv4 addresses located on the subnet. 
2. A for loop is intialized. This loop iterates through all hosts & stores them via the append method in "networkhosts", defined above. 
```sh
networkhosts = []
for host in nmScan.all_hosts():
    networkhosts.append(host)
print(networkhosts)
```
