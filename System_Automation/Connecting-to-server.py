import paramiko

def sshconnect(hostname, port, username, password):
    sshclient = paramiko.SSH 