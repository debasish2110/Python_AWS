import sys
import boto3

option = sys.argv[1]

ec2_client = boto3.client('ec2', region_name='ap-south-1')

if option.lower() == 'create':
    response = ec2_client.run_instances(
            ImageId='ami-062f0cc54dbfd8ef1',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='tf_kp',
            SecurityGroupIds=['sg-0c1c94a22051c3e6e'],
            SubnetId='subnet-03212bd903a2f9ae8',
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': 'MyBoto3Instance'}]
                }
            ]
        )
    print(response)
elif option.lower() == 'terminate':
    response = ec2_client.describe_instances()
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    print(f"fetched instance ids: {instance_ids}")

    response = ec2_client.terminate_instances(InstanceIds=instance_ids)
    print(f"deleted instance response: {response}")




