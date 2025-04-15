import json
import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    
    # Extract file info from the S3 event
    s3_info = event['Records'][0]['s3']
    bucket = s3_info['bucket']['name']
    key = s3_info['object']['key']
    
    # Build dynamic input and output paths
    input_path = f"s3://{bucket}/{key}"
    
    # Optional: You can customize output_path logic if needed
    output_path = "s3://retail-cleaned-output123/parquet_output/"

    # Start Glue job with arguments
    response = glue.start_job_run(
        JobName='your-glue-job-name',  # Replace with your actual Glue job name
        Arguments={
            '--input_path': input_path,
            '--output_path': output_path
        }
    )

    print("✅ Glue job started. Run ID:", response['JobRunId'])
    return {
        'statusCode': 200,
        'body': json.dumps('Glue job triggered successfully!')
    }
