import boto3
import json

def lambda_handler(event,context):
     
 aws_console=boto3.session.Session(profile_name="default")

 s3_client= aws_console.client('s3')

 bucket_name = "manasbucket726"

 response = s3_client.list_objects(Bucket= "bucket_name")

 file_extensions= {}

 for object in response['Contents']:
     file_name= object['Key']
     file_extension= file_name.split('.')[-1]

     file_extensions[file_extension]+=1


 return {
        'statusCode': 200,
        'body': json.dumps(file_extensions)
    }
   
  
