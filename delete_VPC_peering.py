import boto
import boto.vpc
import time
import boto3
from credentials import *

def delete_VPC_Peering_Connection():
    boto.connect_vpc(aws_access_key_id=access,aws_secret_access_key=secret)
    region = boto.vpc.connect_to_region(region_name='us-west-2')
    p_conn = region.get_all_vpc_peering_connections()
    print(p_conn)
    time.sleep(20)
    region.delete_vpc_peering_connection(vpc_peering_connection_id=p_conn[0].id)
    

boto3.resource('ec2')
