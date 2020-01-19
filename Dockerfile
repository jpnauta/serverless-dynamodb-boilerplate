FROM python:3.6-alpine

ADD requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /code/

ADD run.py .
ADD app/ app/

# Add fake credentials to allow connect to dynamodb-local
# https://github.com/serverless/serverless/issues/1518
ENV AWS_ACCESS_KEY_ID 'AWS_ACCESS_KEY_ID'
ENV AWS_SECRET_ACCESS_KEY 'AWS_SECRET_ACCESS_KEY'
ENV AWS_DEFAULT_REGION 'us-west-2'

CMD ["tail", "-f", "/dev/null"]