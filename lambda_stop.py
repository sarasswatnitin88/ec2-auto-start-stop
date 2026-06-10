import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            shutdown_tag = False
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'shutdown' and tag['Value'].lower() == 'false':
                    shutdown_tag = True
                    break
            if shutdown_tag:
                print(f"Skipping: {instance_id}")
            else:
                ec2.stop_instances(InstanceIds=[instance_id])
                print(f"Stopped: {instance_id}")
    
    return {
        'statusCode': 200,
        'body': 'EC2 instances stopped based on shutdown tag'
    }
