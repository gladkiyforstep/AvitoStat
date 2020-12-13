from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger



def myjob():
    print('Every hour job example')


class EveryHourTask:
    def __init__(self, job=myjob):
        self.job = job
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def run(self):
        self.scheduler.add_job(
            self.job,
            trigger=CronTrigger(hour='*'),
            id="myjob",
            jobstore="default",
            replace_existing=True
        )
