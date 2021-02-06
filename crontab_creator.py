#pip install python-crontab
from crontab import CronTab
def set_cron_job(run_type, hours, minutes, dow, dom, month):
    my_cron = CronTab(user = "henriterrasse")
    cmd = 'source ~/Documents/Code/vaccin/.vaccin/bin/activate && python ~/Documents/Code/vaccin/wrapper.py'
    job = my_cron.new(command=cmd)
    if run_type.lower() == "daily":
        job.minute.on(minutes)
        job.hour.on(hours)
    elif run_type.lower() == "weekly":
        job.dow.on(dow)
        job.minute.on(minutes)
        job.hour.on(hours)
    elif run_type.lower() == "monthly":
        job.dom.on(dom)
        job.minute.on(minutes)
        job.hour.on(hours)
    elif run_type.lower() == "yearly":
        job.dom.on(dom)
        job.month.on(month)
        job.minute.on(minutes)
        job.hour.on(hours)
    my_cron.write()
    print(my_cron.render())

set_cron_job("daily", 18, 00, "","","")