import time
def openfile(fname):
    f = open(fname, mode="r")
    ip = f.readlines()
    for x in ip:
        x=x.rstrip('\n')
        print(x)
        time.sleep(3)
    print(fname)

openfile("/root/python/ipaddress")
