import os

def setup_sample_environment():
    # name of the files
    db_name = "sample.db"
    CSV_file_name = "data.csv"
    json_file_name = "data.json"
    report_file_name = "report.pdf"

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add output folder to exporting result
    output_dir = os.path.join(script_dir, "output")

    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Build the path to the SQLite database, JSON and CSV files
    db_path = os.path.join(db_name)
    CSV_file_path = os.path.join(output_dir,CSV_file_name)
    json_file_path = os.path.join(output_dir,json_file_name)
    report_file_path = os.path.join(output_dir,report_file_name)

    # Sample data to be inserted (10 records)
    '''template:
     - id (INTEGER) --> primary key, auto increment 
     - name (TEXT)
     - email (TEXT)
     - zip_code (TEXT)
     - title (TEXT)
    '''
    # create sample of records
    sample_records = [
        ('Mohamed Emad', 'Mohamed@siemens.com', '10001', 'Engineer'),
        ('Mostafa Khaled', 'Mostafa@valeo.com', '10002', 'Manager'),
        ('Abeer Ali zein', 'Abeer@eJad.com', '10003', 'Technician'),
        ('Khaled Morsy nour', 'Khaled@vodafone.com', '10004', 'Engineer'),
        ('Lotfy Elzein', 'Lotfy@orange.com', '10005', 'Analyst'),
        ('Diana Shaker', 'Diana@siemens.com', '10006', 'Director'),
        ('George', 'george@valeo.com', '10007', 'Consultant'),
        ('Hannah Lee', 'hannah@valeo.com', '10008', 'Director'),
        ('Ian Clarke', 'ian@eJad.com', '10009', 'Manager'),
        ('Jasmine Yasser', 'jasmine@siemens.com', '10010', 'Assistant')
    ]

    return {
        'db_path': db_path,
        'CSV_file_path': CSV_file_path,
        'json_file_path': json_file_path,
        'report_file_path': report_file_path,
        'sample_records': sample_records
    }
