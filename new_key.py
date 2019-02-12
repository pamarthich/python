import boto
import boto.ec2
from credentials import *
def creat_keypair():
    conn = boto.connect_ec2(aws_access_key_id=access, aws_secret_access_key=secret)
    region = boto.ec2.connect_to_region('us-west-2')
    k_name = input("Enter the Key pair you need to create")
    try:
        k_list = region.get_all_key_pairs(keynames=k_name)
        key = region.create_key_pair(k_name)
    except boto.exception.EC2ResponseError as ke:
        if ke.error_code == "InvalidKeyPair.NotFound":
            print("Creating Key Pair")
            key = region.create_key_pair(k_name)
            path = "/root/AWS_keys"
            key.save(path)
            print("New Key Pair",k_name,"Created Successfully and is store in the path:",path)
        elif ke.error_code == "InvalidKeyPair.Duplicate":
            print("Key Pair Already Exist:")
creat_keypair()
