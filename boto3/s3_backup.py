import boto3

# Initialize a boto3 S3 resource
s3 = boto3.resource("s3")
bucket_name = "python-for-devops-s"
key_name = "my-backup.tar.gz"
file_name = r"backup/file/path"

def create_bucket(s3):
    try:
        # Create an S3 bucket in a specified region
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'us-east-2'}  # Specify the region
        )
        print("Bucket created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the bucket: {e}")

def list_buckets(s3):
    print("Created Buckets:")
    for bucket in s3.buckets.all():
        print(bucket.name)

def upload_backup(s3, file_name, bucket_name, key_name):
    try:
        # Open the file in binary read mode
        with open(file_name, 'rb') as data:
            # Upload the file to the specified S3 bucket
            s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
        print("Backup uploaded successfully.")
    except Exception as e:
        print(f"An error occurred while uploading the backup: {e}")


create_bucket(s3)
list_buckets(s3)
upload_backup(s3, file_name, bucket_name, key_name)








