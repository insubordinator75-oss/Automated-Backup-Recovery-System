import logging
import os
import datetime

from database.database import create_connection



# ==================================================
# CREATE LOG DIRECTORY
# ==================================================

if not os.path.exists("logs"):

    os.makedirs("logs")



# ==================================================
# LOGGER CONFIGURATION
# ==================================================

logging.basicConfig(

    filename="logs/system.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)





# ==================================================
# CREATE DATABASE LOG + FILE LOG
# ==================================================

def create_log(event, status):


    try:


        connection = create_connection()


        cursor = connection.cursor()



        cursor.execute(

            """
            INSERT INTO system_logs
            (
                event,
                timestamp,
                status
            )

            VALUES(?,?,?)

            """,

            (

                event,

                str(datetime.datetime.now()),

                status

            )

        )



        connection.commit()

        connection.close()



        # Save in system.log

        if status == "Success":


            logging.info(
                event
            )


        else:


            logging.error(
                event
            )



    except Exception as e:


        logging.error(
            f"Logging failed: {e}"
        )







# ==================================================
# GET ALL LOGS FROM DATABASE
# ==================================================

def get_logs():


    try:


        connection = create_connection()


        cursor = connection.cursor()



        cursor.execute(

            "SELECT * FROM system_logs"

        )



        logs = cursor.fetchall()



        connection.close()



        return logs



    except Exception as e:


        logging.error(

            f"Reading logs failed: {e}"

        )


        return []







# ==================================================
# DIRECT FILE LOG FUNCTIONS
# ==================================================

def log_success(message):


    logging.info(

        message

    )




def log_error(message):


    logging.error(

        message

    )