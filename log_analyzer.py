http_500_count = 0
db_timeout_count = 0
info_count = 0
total_lines = 0

try:
    with open('application.log', 'r') as log_file:
        for line in log_file:
            total_lines = total_lines + 1
            if 'HTTP 500' in line:
                http_500_count = http_500_count + 1
            elif 'Database Timeout' in line:
                db_timeout_count = db_timeout_count + 1
            elif '[INFO]' in line:
                info_count = info_count + 1

    with open('incident_report.txt', 'w') as report_file:
        report_file.write("--- Server Diagnostic Summary ---\n")
        report_file.write("Total events processed: " + str(total_lines) + "\n")
        report_file.write("INFO events: " + str(info_count) + "\n")
        report_file.write("HTTP 500 Errors: " + str(http_500_count) + "\n")
        report_file.write("Database Timeouts: " + str(db_timeout_count) + "\n")
        
        report_file.write("\n--- Recommendation ---\n")
        if http_500_count > 0 or db_timeout_count > 0:
            report_file.write("Attention required: Errors detected in the server log.\n")
        else:
            report_file.write("Server is operating normally.\n")

except FileNotFoundError:
    print("Error: The log file 'application.log' was not found.")
except Exception as e:
    print("An unexpected error occurred: " + str(e))
