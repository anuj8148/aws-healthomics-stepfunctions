import json
import boto3

def lambda_handler(event, context):
    # Get S3 bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Create an S3 client
    s3 = boto3.client('s3')

    # Download the JSON file from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    json_data = json.loads(response['Body'].read().decode('utf-8'))

    # Extract relevant information
    flowcellid = json_data['flowcellid']
    qcWorkflowOutputS3Path = json_data['qcWorkflowOutputS3Path']
    qc_reference_s3 = json_data['qc_reference_s3']
    samples = json_data['samples']

    # Prepare data for Step Functions
    step_functions_input = {
        "flowcellid": flowcellid,
        "qcWorkflowOutputS3Path": qcWorkflowOutputS3Path,
        "qc_reference_s3": qc_reference_s3,
        "samples": samples
    }
    

    # Invoke the Step Functions state machine
    step_functions_client = boto3.client('stepfunctions')
    response = step_functions_client.start_execution(
        stateMachineArn='arn:aws:states:us-west-2:210616359528:stateMachine:CarisPoCStepFunctions',
        name=flowcellid,
        input=json.dumps(step_functions_input)
    )

    return {
        'statusCode': 200,
        'body': json.dumps('S3 Trigger Lambda function executed successfully!')
    }
