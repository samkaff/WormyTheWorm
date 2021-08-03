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
