# DataBaseManagementSystem

This project is designed to create a database, export data to CSV and JSON formats, and generate a report in PDF format. The main script, `main.py`, orchestrates these tasks using various utility modules.

## Prerequisites

- Python 3.x
- Python package: "reportlab" (will be installed in Setup section)  

## Setup

1. Clone the repository

    ```bash
    git clone https://github.com/Mohamed-Farag/DataBaseManagement.git
    cd DataBaseManagement
    ```

2. Install the required packages

    ```bash
    pip install reportlab
    ```

3. Set up the environment

    Update the `setupEnvironment.py` script with needed data.

## Usage

1. Run the main script

    ```bash
    python3 main.py
    ```

2. Functionality

    - Configuration and Sample Data
        - The script sets up the environment and retrieves configuration details and sample data using `setupEnvironment.setup_sample_environment()`.

    - Database Operations
        - Connects to the database specified in the configuration.
        - Creates a table and inserts sample data into the database.
        - Exports the data to CSV and JSON formats.

    - Report Generation
        - Generates a report in PDF format using the exported CSV and JSON files.

## File Structure

- `main.py` The main script that coordinates the entire process.
- `setupEnvironment.py` Sets up the environment and provides configuration details and sample data.
- `utils.databaseManager.py` Contains the `DatabaseManager` class for database operations.
- `utils.fileManager.py` Contains the `FileManager` class for CSV and json operations.
- `utils.report.py` Contains the `ReportGenerator` class for generating reports.

## Output

- script will create output folder which contains:
    - `sample.db`: A database file that contain data table with records (e.g. 10 records)
    - `CSV File`: The data is exported to a CSV file
    - `JSON File`: The data is exported to a JSON file
    - `PDF Report`: A report is generated in PDF format and saved to the path specified in the configuration.


