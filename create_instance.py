import os
import time
import boto
import boto.manage.cmdshell
import boto.ec2
from credentials import *

"""access = input("Please enter your access_key:")"""
"""secret = input("Please enter your secret_key:")"""
r_name = "us-west-2"
#key_name = input("Enter the Key Pair to assign to an instance:")


def launch_instance(ami='ami-6cd6f714',
                    instance='t2.micro',
                    key_name='web',
                    key_extension='.pem',
                    key_dir="/root/AWS_keys",
                    group_name='web',
                    ):
    conn = boto.connect_ec2(aws_access_key_id=access, aws_secret_access_key=secret)
    region = boto.ec2.connect_to_region(r_name)
    # creating a new Key Pair for the Instance
    try:
        k_list = region.get_all_key_pairs(keynames=key_name)
        key = region.create_key_pair(key_name)
    except boto.exception.EC2ResponseError as ke:
        if ke.error_code == "InvalidKeyPair.NotFound":
            print("Creating Key Pair")
            key = region.create_key_pair(key_name)
            #path = "/root/AWS_keys"
            key.save(key_dir)
            print("New Key Pair", key_name, "Created Successfully and is store in the path:", key_dir)
        elif ke.error_code == "InvalidKeyPair.Duplicate":
            print("Key Pair Already Exist:")
    # Creating a New Security Group for the instance
    try:
        s_list = region.get_all_security_groups(groupnames=group_name)
        region.create_security_group(name=group_name, description="This is for web servers")
    except boto.exception.EC2ResponseError as se:
        if se.error_code == 'InvalidGroup.NotFound':
            print("creating a security group")
            region.create_security_group(name=group_name, description="This is for web servers")
            print('Security Group', group_name, "created Successfully")
        elif se.error_code == 'InvalidGroup.Duplicate':
            print("Security group already exist, Please proceed if you want to authorize it")
    # Authorizing Security Group
    try:
        s_list = region.get_all_security_groups(groupnames=group_name)
        region.authorize_security_group(group_name=group_name, ip_protocol='tcp', from_port=22, to_port=22,
                                        cidr_ip='0.0.0.0/0')
    except boto.exception.EC2ResponseError as se:
        if se.error_code == 'InvalidGroup.NotFound':
            print("Security Group Not Exist")
    # Creating an Instance
    res = region.run_instances(image_id=ami, min_count=1, key_name=key_name, instance_type=instance, security_group_ids=[group_name])
    instance = res.instances[0]
    status = instance.update()
    while status == "pending":
        print('waiting for instance to come up')
        time.sleep(5)
        instance.update()
    if status == 'running':
        print("adding tag to the instance")
        instance.add_tag("Name","Puppet Server")
    else:
        print('Instance status:' + status)



launch_instance()