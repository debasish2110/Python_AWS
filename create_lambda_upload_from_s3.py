import boto3

lambda_Client = boto3.client('lambda', region_name='ap-south-1')
response = lambda_Client.create_function(
    Code={
        'S3Bucket': 'qwertyuoasdfghil',
        'S3Key': 'lambda.zip',
    },
    Description='Process image objects from Amazon S3.',
    FunctionName='test-my-function',
    Handler='main.lambda_handler',
    Publish=True,
    Role='arn:aws:iam::483216680875:role/lambda-to-sns',
    Runtime='python3.12'
)
