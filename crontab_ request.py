import os 
import sys
import time
import requests
import json
import pandas as pd




# Connect to API
response_API = requests.get('https://healthdata.gov/resource/aitj-yx37.json')
print(response_API.status_code)

# Get data from API
data = response_API.text

# put data in json format
json.loads(data)
# you can also load in the data with pd.read_json
# df1 = pd.read_json('https://data.cdc.gov/api/views/b36e-ru3r/rows.json?accessType=DOWNLOAD')

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/data/crontab_request' + nowStr + '.csv', 'w') as f:
    f.write(str(data))


    
