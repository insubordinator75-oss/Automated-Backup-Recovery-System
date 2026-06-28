from reportlab.lib.pagesizes import letter

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet


from monitoring.logger import get_logs




def create_pdf_report():


    file_path = "reports/backup_report.pdf"



    document = SimpleDocTemplate(
        file_path,
        pagesize=letter
    )



    elements = []



    styles = getSampleStyleSheet()



    title = Paragraph(
        "Automated Backup System Report",
        styles["Title"]
    )


    elements.append(title)



    logs = get_logs()



    data = [

        [
            "ID",
            "Event",
            "Timestamp",
            "Status"
        ]

    ]



    for log in logs:

        data.append(
            list(log)
        )



    table = Table(data)


    elements.append(table)



    document.build(
        elements
    )



    return file_path