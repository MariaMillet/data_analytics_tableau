import boto3 
s3_client = boto3.client('s3')

# upload combined_data to aws S3 bucket
# response = s3_client.upload_file(file_name, bucket, object_name)
# response = s3_client.upload_file('combined_data/combined_data.csv', 'data-analytics-tabl', 'combined_data.csv')

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('data-analytics-tabl')

for file in my_bucket.objects.all():
    print(file.key)