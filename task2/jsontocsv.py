import json
import boto3
import boto3.session
import csv


def json_to_csv(json_content, csv_file_path):
     keys = json_content[0].keys()
     with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(json_content)


def lambda_handler(event, context):
    aws_console= boto3.session.Session(profile_name="default")
    s3_client=aws_console.client('s3')

    input_bucket= "manasbucket726"
    output_bucket= "anasbucket789"


    json_folder = 'dir-1/test.json'
    

    json_file = s3_client.get_object(Bucket=input_bucket, Key=json_folder)

    json_content=json.loads(json_file['Body'].read().decode('utf-8'))

    csv_file_path= "./test.csv"

    json_to_csv(json_content,csv_file_path)

    with open(csv_file_path, 'rb') as csvfile:
        s3_client.upload_file(csv_file_path, output_bucket,csvfile)


    return {
            'statusCode': 200,
            'body': json.dumps('CSV file has been successfully uploaded.')
        }





