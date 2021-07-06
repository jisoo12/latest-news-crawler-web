import time
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


# sched = BlockingScheduler()
sched = BackgroundScheduler()


@sched.scheduled_job('interval', seconds=5, id='test1')
def job1():
  print("job1 : " + time.strftime("%H:%M:%S"))


print('sched before~')
sched.start()
print('sched after~')


while True:
  time.sleep(1)
