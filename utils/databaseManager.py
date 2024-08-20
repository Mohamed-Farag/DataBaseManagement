import csv
import json
import sqlite3
from sqlite3 import Error

class DatabaseManager:
    def __init__(self, db_file):
        """
        Initialize the DatabaseManager with the database file.
        :param db_file: database file
        """
        self.db_file = db_file
        self.conn = self.create_connection()

    def create_connection(self):
        """
        Create a database connection to the SQLite database specified by db_file.
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(self.db_file)
            print(f"Connected to the database: {self.db_file}")
            return conn
        except Error as e:
            print(f"Error: {e}")
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
            print("Table 'data' created successfully or already exists.")
        except Error as e:
            print(f"Error: {e}")

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
            print(f"{len(data)} records inserted successfully.")
        except Error as e:
            print(f"Error: {e}")

    def export_to_csv(self, output_file):
        """
        Export the data from the 'data' table to a CSV file.
        :param output_file: The path of the CSV file to write to
        :return: None
        """
        try:
            # create a cursor
            cursor = self.conn.cursor()

            # Write a query and execute it with cursor
            query = "SELECT * FROM data"
            cursor.execute(query)

            # Fetch and output result
            rows = cursor.fetchall()

             # Get the headers
            headers = [description[0] for description in cursor.description]
            
            with open(output_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)  # Write headers
                writer.writerows(rows)
            
            print(f"Data exported to {output_file} successfully.")
        except Error as e:
            print(f"Error: {e}")

    def export_to_json(self, output_file):
        """
        Export the data from the 'data' table to a JSON file.
        :param output_file: The path of the JSON file to write to
        :return: None
        """
        try:
            # create a cursor
            cursor = self.conn.cursor()

            # Write a query and execute it with cursor
            query = "SELECT * FROM data"
            cursor.execute(query)

            # Fetch and output result
            rows = cursor.fetchall()

            # Get the headers
            headers = [description[0] for description in cursor.description]
            
            data_list = [dict(zip(headers, row)) for row in rows]
            
            with open(output_file, 'w') as file:
                json.dump(data_list, file, indent=4)
            
            print(f"Data exported to {output_file} successfully.")
        except Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        """
        Close the database connection.
        :return: None
        """
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
