import os 
import sys
import time
import requests
import json
import pandas as pd


df1 = pd.read_json("https://healthdata.gov/resource/aitj-yx37.json")
print(df1)
#df.to_csv('/Users/brittanykusi-gyabaah/Documents/GitHub/crontab/csv_files.csv')


# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/data/crontab_read' + nowStr + '.csv', 'w') as f:
    f.write(str(data))