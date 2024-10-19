"""
This is a script to take backup from local to AWS S3
boto3 --> used to do AWS tasks using Python

"""

import boto3

s3 = boto3.resource("s3")
def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3):
    s3.create_bucket(Bucket="python-for-devops-vaishnavi",
                     CreateBucketConfiguration={
                        'LocationConstraint': 'ap-south-1',
                     },)
    print("bucket created successfully")

def upload_backup(s3,file_name,bucket_name,key_name):

    data = open(r'D:\\Python\\backup\\backup_2024-10-19.tar.gz', 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully")


bucket_name = "python-for-devops-vaishnavi"   
region = "ap-south-1"

#create_bucket(s3)
#show_buckets(s3)
file_name = "D:\Python\backup\backup_2024-10-19.tar.gz"
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz")
   