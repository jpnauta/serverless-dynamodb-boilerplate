from pynamodb.models import Model


class BaseModel(Model):
    class Meta:
        host = 'http://dynamodb:8000'
        region = 'us-west-2'
