## Summary
- when I ran crontab without the direct path to my folder using``` > log.txt 2>&1 & ``` 
- the command worked but the txt. file was now being generated in the main directory
- I added the direct path for the folder I wanted my crontab command to generate but it stopped working

## Things I tried to troubleshoot
- I tried to change .csv to .txt in this line of code | https://github.com/Brittanykusi/crontab/blob/2bbe697aca2232cc6cefd801a2e06bf929dc972e/crontab_read.py#L27-L28
- I tried changing running the command with ``` sudo crontab -e ```