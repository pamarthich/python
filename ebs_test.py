import boto3
import unittest
import Create_EBS as c
client = boto3.client('ec2')
class TestingEbsCreation(unittest.TestCase):
    def test_ebs(self):
        response = c.create_ebs()
        x=response['VolumeID']
        self.assertEqual(x, true)

if __name__=='__main__':
     unittest.main()
