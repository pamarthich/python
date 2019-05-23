import boto3
import json

client = boto3.client('lambda')
response =client.get_function_configuration(FunctionName= "test")
data = response['Environment']['Variables']
for key in data.keys():
    if key == "testnam":
        data[key] = "mumbi"
print(data)

update = client.update_function_configuration(
    FunctionName = 'test',
    Environment= response['Environment']
)

launch = client.invoke(
    FunctionName = "test",
    LogType = "Tail"
)
print(launch)
