import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
volumes = ec2.describe_volumes(Filters=[{
    'Name': 'tag:Name',
    'Values': ['bijay-ec2-cloudformation']
}])

for volume in volumes['Volumes']:
    volume_id = volume['VolumeId']
    response = ec2.create_snapshot(
        Description='This is my volume snapshot, bijay',
        VolumeId=volume_id
    )
print(volumes)


