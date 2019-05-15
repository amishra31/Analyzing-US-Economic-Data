import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

df=pd.read_csv(links["GDP"])
df.head()

df1=pd.read_csv(links["unemployment"])
df1.head()

df2=df1[df1['unemployment']>8.5]
df2.head()

x = df[['date']]

gdp_change = df[['change-current']]

unemployment = df1[['unemployment']]

title = "Unemployment vs GDP Change"

file_name = "index.html"

make_dashboard(x, gdp_change, unemployment, title, file_name)

credentials = {

   "apikey": "your-api-key",

   "cos_hmac_keys": {

    "access_key_id": "your-access-key-here", 

     "secret_access_key": "your-secret-access-key-here"

   },

 
    "endpoints": "your-endpoints",

   "iam_apikey_description": "your-iam_apikey_description",

   "iam_apikey_name": "your-iam_apikey_name",

   "iam_role_crn": "your-iam_apikey_name",

    "iam_serviceid_crn": "your-iam_serviceid_crn",

  "resource_instance_id": "your-resource_instance_id"

}

endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'

bucket_name = 'pythdatascience'

import boto3

resource = boto3.resource(
    's3',
    aws_access_key_id = credentials["cos_hmac_keys"]['access_key_id'],
    aws_secret_access_key = credentials["cos_hmac_keys"]["secret_access_key"],
    endpoint_url = endpoint,
)

import os

directory = os.getcwd()
html_path = directory + "/" + file_name

f=open(html_path,"r")

resource.Bucket(name='pythdatascience').put_object(Key='index.html', Body=f.read())

Params = {'Bucket':"pythdatascience" ,'Key':"index.html" }

import sys
time = 7*24*60**2
client = boto3.client(
    's3',
    aws_access_key_id = credentials["cos_hmac_keys"]['access_key_id'],
    aws_secret_access_key = credentials["cos_hmac_keys"]["secret_access_key"],
    endpoint_url=endpoint,

)

url = client.generate_presigned_url('get_object',Params=Params,ExpiresIn=time)

print(url)