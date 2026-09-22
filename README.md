# Server Log Analyzer

A lightweight Python diagnostic script designed to read server log files, categorize events, and generate a clear incident report.

## Project Overview
This project was built to demonstrate fundamental Python skills, specifically file I/O operations and error handling. It operates strictly using standard, core Python features—without relying on external libraries, Object-Oriented Programming (OOP), list comprehensions, or regular expressions (regex).

## Features
- **Log Parsing**: Reads a simulated `application.log` line-by-line.
- **Categorization**: Identifies and counts standard `[INFO]` events, `HTTP 500` server errors, and `Database Timeout` errors.
- **Diagnostic Reporting**: Automatically generates an `incident_report.txt` with a summary of the events and an automated recommendation.
- **Exception Handling**: Gracefully handles missing files and unexpected runtime errors using `try-except` blocks.

## Usage

1. Ensure Python is installed on your system.
2. Clone this repository to your local machine.
3. Run the script from the command line in the project directory:

    ```bash
    python log_analyzer.py
    ```

4. The script will output an `incident_report.txt` file in the same directory with the analysis results.
