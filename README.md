# crontab
## create python file inserting a json file
- import packages https://github.com/Brittanykusi/crontab/blob/2bbe697aca2232cc6cefd801a2e06bf929dc972e/crontab_read.py#L1-L6
- import JSON file https://github.com/Brittanykusi/crontab/blob/2bbe697aca2232cc6cefd801a2e06bf929dc972e/crontab_read.py#L9
- get current working directory https://github.com/Brittanykusi/crontab/blob/2bbe697aca2232cc6cefd801a2e06bf929dc972e/crontab_read.py#L15
## pull JSON file data and save as csv file with a time stamp
- get the current time https://github.com/Brittanykusi/crontab/blob/2bbe697aca2232cc6cefd801a2e06bf929dc972e/crontab_read.py#L21
- save current time as a string https://github.com/Brittanykusi/crontab/blob/2bbe697aca2232cc6cefd801a2e06bf929dc972e/crontab_read.py#L24
- create a new file in the current working directory https://github.com/Brittanykusi/crontab/blob/2bbe697aca2232cc6cefd801a2e06bf929dc972e/crontab_read.py#L27-L28

## create a new virtual machine on Azure

## get environment ready for crontab
- update environment | ``` sudo apt-get update ```

## run crontab command
- clone git hub repo | ``` git clone 'repository name' ```
- cd into folder containing python file
- run ``` crontab -e ``` to write crontab commands
  - pull data once a day | ``` 0 8 * * * /usr/bin/python3/ home/brittany/crontab/crontab_read.py > home/brittany/crontab/log.txt 2>&1 & ```
  - pull data every Sunday night at 10:00pm | ``` 0 22 * * SUN /usr/bin/python3/ home/brittany/crontab/crontab_read.py > home/brittany/crontab/log.txt 2>&1 & ```
  - pull data at the end of every quarter  | ``` 0 0 1 */3 * /usr/bin/python3/ home/brittany/crontab/crontab_read.py > home/brittany/crontab/log.txt 2>&1 & ```
  - ctrl + o --> enter --> ctrl + o
  - to see the automated file generate | ``` ls -l ```

