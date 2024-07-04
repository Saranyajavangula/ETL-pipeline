import os
from src.extract import extract_data
from src.transform import transform_data
from src.load_to_s3 import load_to_s3
from dotenv import load_dotenv
load_dotenv()
aws_access_key=os.getenv('aws_access_key_id')
aws_secret_access_key=os.getenv('aws_secret_access_key_id')


#extract the data from tables
online_trans=extract_data()
print('the shape of the extracted dataframe',online_trans.shape)
online_trans_cleaned=transform_data(online_trans)
print('the shape of the dataframe after cleaning ',online_trans_cleaned.shape)
#print(online_trans_cleaned.head)

#load the data
key = "etl/la_online_trans_final.csv"
aws_s3_bucket='waia-march-bootcamp'
load_to_s3(online_trans_cleaned,aws_access_key,aws_secret_access_key,key,aws_s3_bucket)