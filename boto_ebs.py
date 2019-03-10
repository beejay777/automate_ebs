import boto3
import requests

response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
instance_id = response.text

ec2 = boto3.client('ec2', region_name='us-east-1')

# takes snapshot of every 'in-use volume'
volumes = ec2.describe_volumes(Filters=[{
    'Name': 'attachment.instance-id',
    'Values': [instance_id]
}])


for volume in volumes['Volumes']:
    volume_id = volume['VolumeId']
    response = ec2.create_snapshot(
        Description='Snapshot through cloudformation.',
        VolumeId=volume_id
    )
print(volumes)


