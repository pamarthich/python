import os
import sys
import platform
import subprocess
import time

plat = platform.system()
script_dir = sys.path[0]
hosts = os.path.join(script_dir,'hosts.txt')
hosts_file = open(hosts, 'r')
lines = hosts_file.readlines()
for i in lines:
    st= i.strip()
    print(st)
    #res = subprocess.call(['ping', st])
    args = ['ping', st]
    ping = subprocess.Popen(args, stdout= subprocess.PIPE, stderr= subprocess.PIPE)
    pr= ping.stdout.read()
    out, error = ping.communicate()
    print(out)
    #print(error)
    if out == 0:
        print("ping to",st,"ok")
    elif out == 2:
        print("npo response from ",st)
    else:
        print("ping to", st, "failed")










