import boto3
#access_key = "AKIAYCNVISPWFHIMQXKU"
#secret_key = "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"
topic_arn = ['arn:aws:sns:ap-south-1:554967798764:avatar', 'arn:aws:sns:ap-south-1:554967798764:chandu']
session = boto3.session.Session(profile_name='avathar', region_name='ap-south-1')

sns = session.client('sns')

def create_topic():
    t_name = raw_input('Enter the topic name to create: `')
    response = sns.create_topic(
        Name= t_name
    )
    print(response)

def delete_topic():
    for topic in topic_arn:
        response = sns.delete_topic(
           TopicArn = topic
    )
    print(response)


print("enter 1 to create topic")
print("enter 2 to delete topic")
choice = raw_input("choose the functionality: ")
if choice == 1 :
    create_topic()
else:
    delete_topic()


