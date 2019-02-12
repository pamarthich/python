import boto
import boto.vpc
from credentials import *
import time
boto.connect_vpc(aws_access_key_id=access,aws_secret_access_key=secret)
region = boto.vpc.connect_to_region(region_name='us-west-2')
def create_VPC_Peering():
    l_vpc = region.get_all_vpcs()
    print(l_vpc)
    time.sleep(10)
    v_conn = region.create_vpc_peering_connection(l_vpc[0].id,l_vpc[1].id)
    print(v_conn)
    print("Reguest raised")
    p_conn = region.get_all_vpc_peering_connections()
    if len(p_conn) != 0:
        approve_Peering_request()
def approve_Peering_request():
    p_conn = region.get_all_vpc_peering_connections()
    print(p_conn)
    time.sleep(10)
    region.accept_vpc_peering_connection(vpc_peering_connection_id=p_conn[0].id)
    print("Peering Request Accepted and Connection is Established")

create_VPC_Peering()