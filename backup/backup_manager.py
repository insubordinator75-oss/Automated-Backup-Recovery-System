import os
import shutil
import datetime
import logging


from database.database import create_connection
from monitoring.logger import create_log



# Backup storage location

BACKUP_FOLDER = "storage/backups"



# ==================================================
# CREATE BACKUP DIRECTORY
# ==================================================

def create_backup_directory():

    if not os.path.exists(BACKUP_FOLDER):

        os.makedirs(BACKUP_FOLDER)





# ==================================================
# GENERATE BACKUP NAME
# ==================================================

def generate_backup_name():

    current_time = datetime.datetime.now()


    return (
        "Backup_"
        +
        current_time.strftime(
            "%Y%m%d_%H%M%S"
        )
    )





# ==================================================
# CALCULATE BACKUP SIZE
# ==================================================

def calculate_size(path):


    total_size = 0


    for root, dirs, files in os.walk(path):


        for file in files:


            file_path = os.path.join(
                root,
                file
            )


            total_size += os.path.getsize(
                file_path
            )


    return round(
        total_size / (1024 * 1024),
        2
    )





# ==================================================
# SAVE BACKUP RECORD
# ==================================================

def save_backup_record(
        source,
        destination,
        size,
        status
):


    connection = create_connection()


    cursor = connection.cursor()



    cursor.execute(

        """

        INSERT INTO backups

        (
        backup_date,
        source_path,
        destination_path,
        backup_size,
        status
        )

        VALUES(?,?,?,?,?)

        """,

        (

        str(datetime.datetime.now()),

        source,

        destination,

        size,

        status

        )

    )



    connection.commit()

    connection.close()





# ==================================================
# MAIN BACKUP FUNCTION
# ==================================================

def create_backup(source_path):


    try:


        # Validate source folder

        if not os.path.exists(source_path):

            raise FileNotFoundError(
                "Source folder does not exist"
            )



        logging.info(
            "Backup process started"
        )



        create_backup_directory()



        backup_name = generate_backup_name()



        destination = os.path.join(

            BACKUP_FOLDER,

            backup_name

        )



        # Copy files

        shutil.copytree(

            source_path,

            destination

        )



        size = calculate_size(

            destination

        )



        save_backup_record(

            source_path,

            destination,

            size,

            "Success"

        )



        create_log(

            "Backup Created Successfully",

            "Success"

        )



        logging.info(

            "Backup created successfully"

        )



        return True





    except Exception as e:



        logging.error(

            f"Backup failed: {e}"

        )



        save_backup_record(

            source_path,

            "",

            0,

            "Failed"

        )



        create_log(

            "Backup Failed",

            "Failed"

        )



        print(
            "Backup Error:",
            e
        )



        return False