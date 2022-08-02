import json
import boto3

region = 'us-east-1'
ec2_res = boto3.resource('ec2', region_name=region)


def lambda_handler(event, context):
    
    action = event["action"]
    ins_tag = event["ins_tag"]
    
    ec2_tag={"Name":"tag:Name", "Values":[ins_tag]}
    
    if action == 'Stop':
        for instance in ec2_res.instances.filter(Filters=[ec2_tag]):
            instance.stop()
        response = "Instances were stopped"
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }