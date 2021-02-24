from crontab import CronTab
from datetime import datetime

cron = CronTab(tab="""* * * * * command""")
job = cron.new(command='../NewsToJson.py')
job.every(1).minutes

myFile = open('../newsJson/append.txt', 'a')
myFile.write('\nAccessed on ' + str(datetime.now()))

cron.write()
