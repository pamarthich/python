import boto
import boto.ec2
from credentials import *

conn = boto.connect_ec2(aws_access_key_id=access,aws_secret_access_key=secret)
region = boto.ec2.connect_to_region('us-west-2')
s_name = input("Enter the Security Group name you want to create:")
def create_security_group():
    try:
        s_list = region.get_all_security_groups(groupnames=s_name)
        region.create_security_group(name=s_name,description="This is for web servers")
    except boto.exception.EC2ResponseError as se:
        if se.error_code == 'InvalidGroup.NotFound':
            print("creating a security group")
            region.create_security_group(name=s_name,description="This is for web servers")
            print('Security Group',s_name,"created Successfully")
        elif se.error_code == 'InvalidGroup.Duplicate':
            print("Security group already exist, Please proceed if you want to authorize it")
            

create_security_group()