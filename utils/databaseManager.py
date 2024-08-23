import csv
import json
import sqlite3
from sqlite3 import Error
import logging

class DatabaseManager:
    def __init__(self, db_file):
        """
        Initialize the DatabaseManager with the database file.
        :param db_file: database file
        """
        self.db_file = db_file
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.conn = self.create_connection()

    def create_connection(self):
        """
        Create a database connection to the SQLite database specified by db_file.
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(self.db_file)
            self.logger.info(f"Connected to the database: {self.db_file}")
            return conn
        except Error as e:
            self.logger.error(f"Error creating connection to database: {e}")
            return None

    def create_table(self):
        """
        Create the 'data' table in the database.
        :return: None
        """
        try:
            cursor = self.conn.cursor()
            query = '''
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                zip_code TEXT NOT NULL,
                title TEXT NOT NULL
            )
            '''
            cursor.execute(query)
            self.logger.info("Table 'data' created successfully or already exists.")
        except Error as e:
            self.logger.error(f"Error creating new table in database: {e}")

    def insert_data(self, data):
        """
        Insert records into the 'data' table.
        :param data: List of tuples, each representing a record
        :return: None
        """
        try:
            cursor = self.conn.cursor()
            cursor.executemany('''
            INSERT INTO data (name, email, zip_code, title)
            VALUES (?, ?, ?, ?)
            ''', data)
            self.conn.commit()
            self.logger.info(f"{len(data)} records inserted successfully.")
        except Error as e:
            self.logger.error(f"Error inserting new table in database: {e}")

    def export_to_csv(self, output_file):
        """
        Export the data from the 'data' table to a CSV file.
        :param output_file: The path of the CSV file to write to
        :return: None
        """
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM data"
            cursor.execute(query)
            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description]
            
            with open(output_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)  # Write headers
                writer.writerows(rows)
            
            self.logger.info(f"Data exported to {output_file} successfully.")
        except Error as e:
            self.logger.error(f"Error exporting to CSV file: {e}")

    def export_to_json(self, output_file):
        """
        Export the data from the 'data' table to a JSON file.
        :param output_file: The path of the JSON file to write to
        :return: None
        """
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM data"
            cursor.execute(query)
            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description]
            data_list = [dict(zip(headers, row)) for row in rows]
            
            with open(output_file, 'w') as file:
                json.dump(data_list, file, indent=4)
            
            self.logger.info(f"Data exported to {output_file} successfully.")
        except Error as e:
            self.logger.error(f"Error exporting to JSON file: {e}")

    def close_connection(self):
        """
        Close the database connection.
        :return: None
        """
        try:  
            if self.conn:
                self.conn.close()
                self.logger.info(f"Database connection is closed successfully.")
        except Error as e:
            self.logger.error(f"Error closing the database connection: {e}")