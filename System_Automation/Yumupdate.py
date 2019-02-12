import paramiko


#def sshConnect(hostname, port, username, password, command):
plat = platform.system()
script_dir = sys.path[0]
hosts = os.path.join(script_dir, 'hosts.txt')
hosts_file = open(hosts, 'r')
lines = hosts_file.readlines()
for i in lines:
    st = i.strip()
    sshClient = paramiko.SSHClient() #Create SSH client instance
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.load_system_host_keys()
    sshClient.connect(st, 22, 'netops', 'ansible')
    stdin, stdout, stderr = sshClient.exec_command('sudo yum update -y')
    print(stdout.read())
#if __name__ == '__main__':
 #   sshConnect('172.31.19.24', 22, 'netops', 'redhat', 'python readlines.py')
