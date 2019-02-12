import boto
import boto.ec2
from credentials import *

def Terminate_Instance():
    conn = boto.connect_ec2(aws_access_key_id=access,aws_secret_access_key=secret)
    region = boto.ec2.connect_to_region('us-west-2')
    region.terminate_instances(instance_ids=input("Enter The Instance ID to Terminate:"))
    #region.terminate_instances(instance_ids='i-02b501a025c15103d')
Terminate_Instance()