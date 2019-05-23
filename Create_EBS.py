import boto3
client = boto3.client('ec2')
def create_ebs():
    response = client.create_volume(Size=1,  VolumeType='gp2', AvailabilityZone='ap-south-1a', Encrypted=False, 
                     TagSpecifications=[
                         {
                            'ResourceType':'volume',
                             'Tags':[
                                 {
                                     'Key': 'Test',
                                     'Value': 'StorageClass'
                                 },
                                 {
                                   'Key': 'Test1',
                                     'Value': 'StorageClass1'
                                 }
                             ]
                         }

                     ])
    print(response['VolumeId'])

create_ebs()
