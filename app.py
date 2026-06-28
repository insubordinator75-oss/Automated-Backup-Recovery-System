import streamlit as st
import pandas as pd


# Reports
from reports.excel_report import create_excel_report
from reports.pdf_report import create_pdf_report


# Backup
from backup.backup_manager import create_backup
from backup.scheduler import start_scheduler


# Recovery
from recovery.restore import (
    get_available_backups,
    restore_backup
)


# Monitoring
from monitoring.logger import get_logs



# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Automated Backup System",
    page_icon="📦",
    layout="wide"
)



# ==================================================
# HEADER
# ==================================================

st.title(
    "📦 Automated Backup & Recovery System"
)


st.caption(
    "Secure | Automated | Reliable Data Management Platform"
)


st.divider()



# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title(
    "Navigation"
)


menu = st.sidebar.radio(
    "Select Option",
    [
        "🏠 Dashboard",
        "💾 Create Backup",
        "♻ Restore Backup",
        "📁 Backup History",
        "📜 System Logs",
        "⏰ Scheduler",
        "📊 Reports"
    ]
)



st.sidebar.divider()


st.sidebar.info(
    """
    Internship Project

    Project:
    Automated Backup System


    Technology:

    Python
    Streamlit
    SQLite
    """
)



# ==================================================
# DASHBOARD
# ==================================================

if menu == "🏠 Dashboard":


    st.subheader(
        "System Overview"
    )


    backups = get_available_backups()

    logs = get_logs()



    col1, col2, col3 = st.columns(3)



    with col1:

        st.metric(
            "Total Backups",
            len(backups)
        )



    with col2:

        st.metric(
            "System Status",
            "Online"
        )



    with col3:

        st.metric(
            "Total Logs",
            len(logs)
        )



    st.divider()



    st.subheader(
        "Recent Backup Versions"
    )



    if backups:


        for backup in backups[-5:]:

            st.success(
                f"📁 {backup}"
            )


    else:

        st.warning(
            "No backups available"
        )




# ==================================================
# CREATE BACKUP
# ==================================================

elif menu == "💾 Create Backup":


    st.subheader(
        "Create New Backup"
    )


    source = st.text_input(
        "Enter Source Folder Path",
        placeholder="Example: test_data"
    )



    if st.button(
        "🚀 Start Backup",
        use_container_width=True
    ):


        if source:


            with st.spinner(
                "Creating Backup..."
            ):


                result = create_backup(
                    source
                )



            if result:


                st.success(
                    "Backup Created Successfully"
                )


            else:


                st.error(
                    "Backup Failed"
                )



        else:


            st.warning(
                "Please enter folder path"
            )





# ==================================================
# RESTORE BACKUP
# ==================================================

elif menu == "♻ Restore Backup":


    st.subheader(
        "Restore Backup"
    )



    backups = get_available_backups()



    if backups:


        selected_backup = st.selectbox(
            "Select Backup Version",
            backups
        )



        restore_location = st.text_input(
            "Restore Location",
            "restored_data"
        )



        if st.button(
            "♻ Restore",
            use_container_width=True
        ):



            result = restore_backup(
                selected_backup,
                restore_location
            )



            if result:


                st.success(
                    "Restore Completed Successfully"
                )


            else:


                st.error(
                    "Restore Failed"
                )



    else:


        st.info(
            "No backup available"
        )





# ==================================================
# BACKUP HISTORY
# ==================================================

elif menu == "📁 Backup History":


    st.subheader(
        "Backup History"
    )


    backups = get_available_backups()



    if backups:


        dataframe = pd.DataFrame(

            backups,

            columns=[
                "Backup Name"
            ]

        )


        st.dataframe(

            dataframe,

            use_container_width=True

        )



    else:


        st.warning(
            "No backup found"
        )





# ==================================================
# SYSTEM LOGS
# ==================================================

elif menu == "📜 System Logs":


    st.subheader(
        "System Activity Logs"
    )



    logs = get_logs()



    if logs:



        dataframe = pd.DataFrame(

            logs,

            columns=[

                "ID",
                "Event",
                "Timestamp",
                "Status"

            ]

        )


        st.dataframe(

            dataframe,

            use_container_width=True

        )



    else:


        st.info(
            "No logs available"
        )





# ==================================================
# SCHEDULER
# ==================================================

elif menu == "⏰ Scheduler":


    st.subheader(
        "Automatic Backup Scheduler"
    )


    st.write(
        "Run automatic backups in background"
    )



    st.info(
        """
        Current Testing Schedule:

        Backup runs every 1 minute.

        You can later change it to daily/weekly.
        """
    )



    if st.button(
        "▶ Start Scheduler",
        use_container_width=True
    ):



        result = start_scheduler()



        if result:


            st.success(
                "Scheduler Started Successfully"
            )


        else:


            st.error(
                "Scheduler Failed"
            )





# ==================================================
# REPORTS
# ==================================================

elif menu == "📊 Reports":


    st.subheader(
        "Generate & Download Reports"
    )


    st.write(
        "Export backup activities into Excel and PDF formats"
    )


    col1, col2 = st.columns(2)



    # ================= EXCEL REPORT =================


    with col1:


        st.markdown(
            "### 📗 Excel Report"
        )


        if st.button(
            "Generate Excel Report",
            use_container_width=True
        ):


            excel_file = create_excel_report()


            st.success(
                "Excel Report Generated Successfully"
            )


            # Open file

            with open(
                excel_file,
                "rb"
            ) as file:


                st.download_button(

                    label="⬇ Download Excel Report",

                    data=file,

                    file_name="backup_report.xlsx",

                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

                    use_container_width=True

                )





    # ================= PDF REPORT =================


    with col2:


        st.markdown(
            "### 📕 PDF Report"
        )


        if st.button(
            "Generate PDF Report",
            use_container_width=True
        ):


            pdf_file = create_pdf_report()


            st.success(
                "PDF Report Generated Successfully"
            )


            # Open file

            with open(
                pdf_file,
                "rb"
            ) as file:


                st.download_button(

                    label="⬇ Download PDF Report",

                    data=file,

                    file_name="backup_report.pdf",

                    mime="application/pdf",

                    use_container_width=True

                )