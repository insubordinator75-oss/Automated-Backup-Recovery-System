import pandas as pd

from monitoring.logger import get_logs



def create_excel_report():

    logs = get_logs()


    df = pd.DataFrame(

        logs,

        columns=[
            "ID",
            "Event",
            "Timestamp",
            "Status"
        ]

    )


    file_path = "reports/backup_report.xlsx"


    df.to_excel(

        file_path,

        index=False

    )


    return file_path