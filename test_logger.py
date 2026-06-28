from monitoring.logger import (
    create_log,
    get_logs
)


create_log(
    "Testing Logger",
    "Success"
)


logs = get_logs()


for log in logs:

    print(log)