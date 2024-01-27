import boto3
import shutil
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_file_path, bucket_name, s3_file_path):
    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Upload the file
        s3.upload_file(local_file_path, bucket_name, s3_file_path)
        print(f"File uploaded successfully to {bucket_name}/{s3_file_path}")
    except FileNotFoundError:
        print(f"The file {local_file_path} was not found.")
    except NoCredentialsError:
        print("Credentials not available.")

# Example usage
local_model_path = 'models/model.joblib'
s3_bucket_name = 'nyc-taxi-trip-bykhan'
s3_file_path = 'models/model.joblib' 

upload_to_s3(local_model_path, s3_bucket_name, s3_file_path)
shutil.copy(local_model_path, 'model.joblib') 
#we are pushing model.joblib to our folder so that it can be on github and
#from that docker can create image using that as fetching from s3 is not 
#happening by docker, for that we have to hardcode the credentials that is
#not a godd practice (try to resolve this yourself)