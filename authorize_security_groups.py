import boto
import boto.ec2
from credentials import *
from create_security_group import create_security_group

conn = boto.connect_ec2(aws_access_key_id=access,aws_secret_access_key=secret)
region = boto.ec2.connect_to_region('us-west-2')
s_name = input("Enetr the Security Group Name to Authorize:")
try:
    s_list = region.get_all_security_groups(groupnames=s_name)
    region.authorize_security_group(group_name=s_name,ip_protocol='tcp',from_port=8081,to_port=8081,cidr_ip='0.0.0.0/0')
except boto.exception.EC2ResponseError as se:
    if se.error_code == 'InvalidGroup.NotFound':
        print("Security Group Not Exist")
#this is my first comment   
# this is my second comment from GUI
