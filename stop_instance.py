import boto
import boto.ec2
#from credentials import *
#conn = boto.connect_ec2(aws_access_key_id=access,aws_secret_access_key=secret)
region = boto.ec2.connect_to_region('us-west-2')
def stop_instance():
    region.stop_instances(instance_ids=["i-08cb223dac98a7022","i-0db2e603e191fdc79"])
    region.get_all_instances()
    print("Instances Stopped Successfully")


stop_instance()
