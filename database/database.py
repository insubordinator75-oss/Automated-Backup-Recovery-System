import sqlite3
import os


DATABASE_FOLDER = "database"

DATABASE_NAME = "backup_system.db"

DATABASE_PATH = os.path.join(
    DATABASE_FOLDER,
    DATABASE_NAME
)



def create_connection():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    return connection



def create_backup_table():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS backups
    (
        backup_id INTEGER PRIMARY KEY AUTOINCREMENT,
        backup_date TEXT,
        source_path TEXT,
        destination_path TEXT,
        backup_size REAL,
        status TEXT
    )
    """)


    connection.commit()

    connection.close()



def create_recovery_table():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recovery
    (
        recovery_id INTEGER PRIMARY KEY AUTOINCREMENT,
        backup_id INTEGER,
        recovery_date TEXT,
        restored_files TEXT,
        status TEXT,
        recovery_logs TEXT
    )
    """)


    connection.commit()

    connection.close()



def create_logs_table():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system_logs
    (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        event TEXT,
        timestamp TEXT,
        status TEXT
    )
    """)


    connection.commit()

    connection.close()



def initialize_database():

    create_backup_table()

    create_recovery_table()

    create_logs_table()



if __name__ == "__main__":

    initialize_database()

    print("Database Created Successfully")