# loading to s3 docket
import boto3
from io import StringIO


def load_to_s3(df, aws_access_key, aws_secret_access_key, key, aws_s3_bucket):
    s3_conn = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_access_key

    )
    csv_buffer = StringIO()  # create buffer to temporarily store the Data Frame
    df.to_csv(csv_buffer, index=False)  # code to write the data frame as csv file
    s3_conn.put_object(
        Bucket=aws_s3_bucket, Key=key, Body=csv_buffer.getvalue()
    )  # this code writes the temp stored csv file and writes to s3
    print('connection made and loaded to s3')
