import os
import shutil
import datetime

from database.database import create_connection
from monitoring.logger import create_log


BACKUP_FOLDER = "storage/backups"



def get_available_backups():

    if not os.path.exists(BACKUP_FOLDER):

        return []


    return os.listdir(
        BACKUP_FOLDER
    )



def verify_backup(backup_name):

    path = os.path.join(
        BACKUP_FOLDER,
        backup_name
    )


    return os.path.exists(path)



def save_recovery_record(
        backup_id,
        files,
        status,
        logs
):
    create_log(
    "Backup Restored Successfully",
    "Success"
)

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
    """

    INSERT INTO recovery
    (
        backup_id,
        recovery_date,
        restored_files,
        status,
        recovery_logs
    )

    VALUES(?,?,?,?,?)

    """,

    (
        backup_id,
        str(datetime.datetime.now()),
        files,
        status,
        logs
    ))


    connection.commit()

    connection.close()



def restore_backup(
        backup_name,
        restore_location
):

    try:

        backup_path = os.path.join(
            BACKUP_FOLDER,
            backup_name
        )


        if not verify_backup(
            backup_name
        ):

            return False



        shutil.copytree(
            backup_path,
            restore_location
        )


        save_recovery_record(
            0,
            backup_name,
            "Success",
            "Restored successfully"
        )


        return True



    except Exception as e:


        save_recovery_record(
            0,
            backup_name,
            "Failed",
            str(e)
        )


        return False