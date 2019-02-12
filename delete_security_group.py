import boto
import boto.ec2
from credentials import *
import time


def delete_security_group():
    conn= boto.connect_ec2(aws_access_key_id=access,aws_secret_access_key=secret)
    region = boto.ec2.connect_to_region('us-west-2')
    s_list = region.get_all_security_groups()
    print(s_list)
    for x in range(1,19):
        if x == 16:
            continue
        s_name = "launch-wizard-"+format(x)
        region.delete_security_group(name=s_name)
        print("Deleted Security group", s_name)
        time.sleep(5)


delete_security_group()