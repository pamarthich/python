import boto
import boto.ec2
import django

boto.connect_ec2(aws_access_key_id=access, aws_secret_access_key=secret)
region = boto.ec2.connect_to_region('us-west-2')
res = region.get_all_instances()
for i in res:
    print(i.__dict__)
print(res)
print(res.instances.id[0])
