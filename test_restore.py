from recovery.restore import (
    get_available_backups,
    restore_backup
)


print(
    get_available_backups()
)


result = restore_backup(

    "Backup_20260622_171841",

    "restored_data"

)


print(result)