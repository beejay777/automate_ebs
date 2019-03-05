import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
'''
instances = ec2.describe_instance(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']
}])

instance.Reservations.Instances.InstanceId

for instance in instances['Reservations']:
    instanceid = instance['Instances'][0]
'''
# takes snapshot of every 'in-use volume'
volumes = ec2.describe_volumes(Filters=[{
    'Name': 'status',
    'Values': ['in-use']
}])


for volume in volumes['Volumes']:
    volume_id = volume['VolumeId']
    response = ec2.create_snapshot(
        Description='Snapshot through cloudformation.',
        VolumeId=volume_id
    )
print(volumes)


