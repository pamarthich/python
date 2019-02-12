import boto
import boto.ec2
from credentials import *

def start_instances():
    conn = boto.connect_ec2(aws_access_key_id=access,aws_secret_access_key=secret)
    region = boto.ec2.connect_to_region('us-west-2')
    region.start_instances(instance_ids='i-02b501a025c15103d')
    region.start_instances(instance_ids=input("Enter the instance ID to start:"))

start_instances()