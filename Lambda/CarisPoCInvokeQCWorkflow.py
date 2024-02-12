import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

# Initiate client
try:
    print("Attempt to initiate client")
    omics_session = boto3.Session()
    omics_client = omics_session.client('omics')
    print("Attempt to initiate client complete")
except Exception as e:
    raise e

def lambda_handler(event, context):
    R2RworkflowId = event['qcworkflowid']
    role_arn = event['JobRoleArn']
    output_s3_path = event['qcOutputS3Path']
    params = {
        "fasta_path": event['fasta_path']
    }

    try:
        print("Attempt to start workflow run")
        response = omics_client.start_run(
            workflowId=R2RworkflowId,
            workflowType="READY2RUN",
            name=R2RworkflowId + '-QCworkflow',
            roleArn=role_arn,
            parameters=params,
            outputUri=output_s3_path
            )
    except ClientError as e:
        raise Exception( "boto3 client error : " + e.__str__())
    except Exception as e:
       raise Exception( "Unexpected error : " +    e.__str__())
    logger.info(response)
    return {"WorkflowRunId": response['id']}