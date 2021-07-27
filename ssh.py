#!/usr/bin/env python3

import paramiko
# paramiko = python implementation of SSHv2 protocol; documentation @ docs.paramiko.org
# references = https://www.kite.com/python/answers/how-to-ssh-into-a-server-in-python & https://support.sciencelogic.com/s/article/1440

# set variables to be interpreted by paramiko sshclient (host, port, username, password)
host ="10.0.0.94"
port = 22
username = "stephen"
password = "stephen"

#define command variable
command = "mkdir Wormy; cd ~/Wormy; touch 'WormyWasHere'"

# define client/ssh variable to call sshclient
ssh = paramiko.SSHClient()
# set missing host key policy to allow script to SSH into a serve w/ unknown host keys; reference AutoAddPolicy to add above variables when calling SSH
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# connect to client
ssh.connect(host, port, username, password)

# execute command & return 3 tuple (stdin, stdout, stderr)
stdin, stdout, stderr = ssh.exec_command(command)
#return stdout
for lines in stdout: 
    print(line)

