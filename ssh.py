import os
import pipes
import sys
import subprocess
import paramiko

def chpasswd(user, passwd):
    ssh_conn=paramiko.SSHClient()
    ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_conn.load_system_host_keys()
    ssh_conn.connect(hostname='13.234.116.126', port=22, username='test', password='testing')
    proc=subprocess.Popen(
        ['/usr/sbin/chpasswd'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    print("changing:"+user+':'+ passwd)
    out, err=proc.communicate(user + ':' + passwd )
    print(out)
    if proc.returncode !=0:
        print("Error: Return code", proc.returncode, ", stderr: ", out, err)
        if out:
            syslog.syslog("stdout: " + out)
        if err:
            syslog.syslog("stderr: " + err)


chpasswd('buddy', 'teddy')
