from apscheduler.schedulers.background import BackgroundScheduler

from backup.backup_manager import create_backup



scheduler = BackgroundScheduler()



def scheduled_backup():

    source_folder = "test_data"


    result = create_backup(
        source_folder
    )


    if result:

        print(
            "Automatic Backup Completed"
        )

    else:

        print(
            "Automatic Backup Failed"
        )



def start_scheduler():


    scheduler.add_job(

        scheduled_backup,

        "interval",

        minutes=1,

        id="backup_job",

        replace_existing=True

    )


    if not scheduler.running:

        scheduler.start()


    return True