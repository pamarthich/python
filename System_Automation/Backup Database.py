import os
import time
import datetime
import pipes
import sys
import paramiko
import subprocess

def ssh_client():
    db_name = "devops"
    date = time.strftime('%Y-%m-%d')
    ssh_conn = paramiko.SSHClient()
    ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_conn.load_system_host_keys()
    ssh_conn.connect(hostname='172.31.34.108', port=22, username='netops', password='netops')
    dump_cmd = "sudo mysqldump --databases " + db_name + " -u root -p > " + db_name + "_" + date + ".sql"
    subprocess.call(dump_cmd)
    stdin, stdout, stderr = ssh_conn.exec_command(dump_cmd)
    print(stdout)

#db_host = input("Enter the hostname: ")
db_user = 'root'
db_user_password = 'ubuntu'
db_name = 'devops'
dump_cmd = "mysqldump -h  " + db_name +  "  -u" + db_user + "  -p" + db_user_password
print(dump_cmd)
os.system()

time.sleep(10)
try:
    backup_path = os.path.join(sys.path[0], 'db_backup')
    os.path.exists(backup_path)
except:
    print("Path Doesnot exist")
date_time = time.strftime('%Y.%m.%d-%H:%M:%S')
current_path = backup_path + '\\' + date_time
try:
    os.stat(current_path)
except:
    os.mkdir(current_path)
#code to check if need to take backup of multiple dbs or single db

if os.path.exists(db_name):
    file1 = open(db_name)
    multi = 1
    print("Database file found...")
    print("started backup of dbs listed in the file"+db_name)
else:
    print("Database file not found....")
    print("starting backup of database" + db_name)
    multi = 0
if multi == 1:
    r_file = file1.readlines()
    for line in r_file:
        st = line.strip()
        ssh_client()