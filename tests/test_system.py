import os

from backup.backup_manager import create_backup



def test_backup():


    result = create_backup(
        "test_data"
    )


    assert result == True



def test_folder_exists():


    assert os.path.exists(
        "test_data"
    )