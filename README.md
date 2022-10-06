# crontab
## create python file with json file
## pull data once a day 
- 0 8 * * * python3 /crontab/crontab_read.py
## pull data every Sunday night at 10:00pm 
- 0 22 * * SUN python3 /crontab/crontab_read.py
## pull data at the end of every quarter  
- 0 0 1 */3 * python3 /crontab/crontab_read.py
