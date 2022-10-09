import boto3


class DynamoDB(object):
    def __init__(self):
        self.aws_secret_access_key = None
        self.aws_access_key_id = None
        self.region_name = None
        self.endpoint_url = None
        self.resource = None

    def init_app(self, app):
        self.aws_access_key_id = app.config.get('AWS_ACCESS_KEY_ID')
        self.aws_secret_access_key = app.config.get('AWS_SECRET_ACCESS_KEY')
        self.region_name = app.config.get('AWS_REGION_NAME')
        self.endpoint_url = app.config.get('DYNAMODB_ENDPOINT_URL')

        if not self.endpoint_url:
            self.resource = boto3.resource(
                'dynamodb',
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
                region_name=self.region_name
            )
        else:
            self.resource = boto3.resource(
                'dynamodb',
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
                region_name=self.region_name,
                endpoint_url=self.endpoint_url
            )

        return self.resource
