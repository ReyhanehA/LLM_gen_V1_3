#9.# CWE-798: Use of Hard-coded AWS Credentials
# Vulnerable line: s3 = boto3.resource('s3', aws_access_key_id='myaccesskey', aws_secret_access_key='mysecretkey')
# Description: The AWS credentials are hard-coded in the code, making them easily accessible to attackers.

import boto3

s3 = boto3.resource('s3', aws_access_key_id='myaccesskey', aws_secret_access_key='mysecretkey')
bucket = s3.Bucket('mybucket')
for obj in bucket.objects.all():
    print(obj.key)