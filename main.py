import os, time
from handlers.sensors import SensorsHandler
from apscheduler.schedulers.blocking import BlockingScheduler
from log import log
if __name__ == "__main__":
    os.environ['TZ'] = 'Europe/Paris' # set new timezone
    time.tzset()
    log.info("Launching script")
    scheduler = BlockingScheduler(timezone="Europe/Paris")
    sh=SensorsHandler()
    log.info("initiating jobs")
    scheduler.add_job(sh.run, "interval", seconds=60, misfire_grace_time=10)
    log.info(f"jobs added : {scheduler.get_jobs()}")
    scheduler.start()
    log.info("running...")
