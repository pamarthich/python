import boto
import boto.ec2
from credentials import *
import time

def launch_Instance():
    conn = boto.connect_ec2(aws_access_key_id=access,aws_secret_access_key=secret)
    region = boto.ec2.connect_to_region('us-west-2')
    res = region.run_instances(image_id="ami-6cd6f714",min_count=1,key_name='CI',instance_type='t2.micro',security_group_ids=['launch-wizard-19'])
    instance = res.instances[0]
    status = instance.update()
    while status == 'pending':
        time.sleep(10)
        status = instance.update()
    if status == 'running':
        instance.add_tag("Name","Delete Instance")
    else:
        print('Instance status:' + status)

launch_Instance()