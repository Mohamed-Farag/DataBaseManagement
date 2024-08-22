# DataBaseManagementSystem

This project is designed to create a database, export data to CSV and JSON formats, and generate a report in PDF format. The main script, `main.py`, orchestrates these tasks using various utility modules.

## Prerequisites

- Python 3.x

## Setup

1. Clone the repository

    ```bash
    git clone https://github.com/Mohamed-Farag/DataBaseManagementSystem.git
    cd DataBaseManagementSystem
    ```

2. Install the required packages

    ```bash
    pip install reportlab
    ```

3. Set up the environment
    Update the `setupEnvironment.py` script with needed data.

4. (Optional) Prevent Python from creating `.pyc` files

    ```bash
    set PYTHONDONTWRITEBYTECODE=1
    ```

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

## Libraries Used
- `os`: Operating system interfaces
- `csv`: CSV file handling
- `json`: JSON data handling
- `logging`: Logging facility
- `sqlite3`: SQLite database library
- `reportlab`: Library for generating PDFs
- `unittest`: Unit testing framework
- `unittest.mock`: Mocking library for unit tests

## File Structure

- `main.py` The main script that coordinates the entire process.
- `setupEnvironment.py` Sets up the environment and provides configuration details and sample data.
- `utils/databaseManager.py` Contains the `DatabaseManager` class for database operations.
- `utils/fileManager.py` Contains the `FileManager` class for CSV and JSON operations.
- `utils/report.py` Contains the `ReportGenerator` class for generating reports.

## Output

The script will create an output folder which contains:
- `sample.db`: A database file that contains a data table with records (e.g., 10 records)
- `CSV File`: The data is exported to a CSV file
- `JSON File`: The data is exported to a JSON file
- `PDF Report`: A report is generated in PDF format and saved to the path specified in the configuration.
