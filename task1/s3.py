import boto3.session
import boto3
import json

aws_console=boto3.session.Session(profile_name="default")

s3_client= aws_console.client('s3')
bucket_name="manasbucket726"

files_upload = {'dir1' : ['path/test.json', 'path/test.txt', 'path/test.pdf' ],
                'dir2' :['path/dummy.doc', 'path/tmp.raw']}



def uploadfile(files, bucket):
   for dir,file_paths in files.items():
        for file_path in file_paths:
          file_name=file_path.split('/')[-1]
          s3_client.upload_file(file_path,bucket,f'{dir}/{file_name}')


if __name__=='__main__':
   uploadfile(files_upload, bucket_name)        
     
