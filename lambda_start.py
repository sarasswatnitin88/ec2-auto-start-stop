import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['stopped']},
            {'Name': 'tag:Name', 'Values': ['se45rver']}
        ]
    )
    
    started = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2.start_instances(InstanceIds=[instance_id])
            print(f"Started: {instance_id}")
            started.append(instance_id)
    
    return {
        'statusCode': 200,
        'body': f'Started instances: {started}'
    }
