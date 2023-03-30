import os
import boto3

session = boto3.Session()
credentials = session.get_credentials()
default_region = "eu-west-2"

# Check if an environment variable is set
if 'AWS_ACCESS_KEY_ID' in os.environ:
    access_key = os.environ['AWS_ACCESS_KEY_ID']
elif credentials.access_key is not None:
    access_key = credentials.access_key
else:
    raise Exception("AWS_ACCESS_KEY_ID is not provided")

if 'AWS_SECRET_ACCESS_KEY' in os.environ:
    secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
elif credentials.secret_key is not None:
    secret_key = credentials.secret_key
else:
    raise Exception("AWS_SECRET_ACCESS_KEY is not provided")

if 'AWS_REGION' in os.environ:
    region = os.environ['AWS_REGION']
elif session.region_name is not None:
    region = session.region_name
else:
    print(f"WARNING: AWS_REGION is not provided, setting {default_region} as default")
    region = default_region


ec2 = boto3.client('ec2',
                   aws_access_key_id = access_key,
                   aws_secret_access_key = secret_key,
                   region_name = region)

# Use the client to get information about instances
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-code',
            'Values': ['16']
        },
        {
            'Name': 'tag:k8s.io/role/master',
            'Values': ['1']
        }
    ]
)

# Extract the instance information from the response
instances = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instances.append(instance)

# Print the instance IDs and instance names
for instance in instances:
    instance_id = instance['InstanceId']
    instance_name = next((tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Name'), 'Unnamed')
    print("Instance ID: {}, Instance Name: {}".format(instance_id, instance_name))