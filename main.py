from utils import databaseManager
from utils import report
import setupEnvironment

def main():

    # Get the configuration and sample data
    config = setupEnvironment.setup_sample_environment()

    # Access and get the values
    db_path = config['db_path']
    CSV_file_path = config['CSV_file_path']
    json_file_path = config['json_file_path']
    report_file_path = config['report_file_path']
    sample_records = config['sample_records']

    # connect to database
    db_manager = databaseManager.DatabaseManager(db_path)

    # Create the table
    db_manager.create_table()

    # Insert data
    db_manager.insert_data(sample_records)

    # Export data to CSV to output folder (data.csv)
    db_manager.export_to_csv(CSV_file_path)

    # Export data to JSON to output folder (data.json)
    db_manager.export_to_json(json_file_path)

    # Close the connection
    db_manager.close_connection()

    # Generate report to output folder (report.pdf)
    report_generator = report.ReportGenerator(CSV_file_path, json_file_path, report_file_path)
    report_generator.generate_report()

if __name__ == '__main__':
    main()
