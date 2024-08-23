import os
import unittest
from unittest.mock import patch
from databaseManager import DatabaseManager
from sqlite3 import Error
import logging
class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

        # Initialize the DatabaseManager
        self.db_manager_test = DatabaseManager('test_sample.db')
        
        # Create the table before each test
        self.db_manager_test.create_table()


    def test_create_connection(self):
        # Test that the connection is created
        self.assertIsNotNone(self.db_manager_test.conn)
        self.logger.info("test_create_connection: passed")

    @patch('sqlite3.connect', side_effect=Error("Mocked connection error"))
    def test_create_connection_exception(self, mock_connect):
        # Test that the connection fails and None is returned
        db_manager_test = DatabaseManager('sample.db')
        self.assertIsNone(db_manager_test.conn)
        mock_connect.assert_called_once()
        self.logger.info("test_create_connection_exception: Exception handling test passed.")

    def test_create_table(self):
        # Test that the create_table method executes the correct SQL query
        self.db_manager_test.create_table()
        cursor = self.db_manager_test.conn.cursor()

        # The query checks the sqlite_master table,
        # which is a system table in SQLite that stores metadata about the database schema,
        # including information about tables, indexes, and other objects.
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='data';")

        table_exists = cursor.fetchone()
        self.assertIsNotNone(table_exists)
        self.logger.info("test_create_table: Table creation test passed.")


    def test_insert_data(self):
        # Sample data to insert
        sample_data = [
            ('John Doe', 'john@example.com', '12345', 'Manager'),
            ('Jane Smith', 'jane@example.com', '67890', 'Developer')
        ]
        
        # Insert data
        self.db_manager_test.insert_data(sample_data)
        
        # Verify data insertion
        cursor = self.db_manager_test.conn.cursor()
        cursor.execute("SELECT * FROM data")
        rows = cursor.fetchall()
        
        self.assertEqual(len(rows), len(sample_data))

        # Check the content of each row
        for i, row in enumerate(rows):
            self.assertEqual(row[1], sample_data[i][0])  # Name
            self.assertEqual(row[2], sample_data[i][1])  # Email
            self.assertEqual(row[3], sample_data[i][2])  # Phone
            self.assertEqual(row[4], sample_data[i][3])  # Position
        
        self.logger.info("test_insert_data: Data insertion test passed.")


    def test_export_to_csv(self):
        # Sample data to insert
        sample_data = [
            ('John Doe', 'john@example.com', '12345', 'Manager'),
            ('Jane Smith', 'jane@example.com', '67890', 'Developer')
        ]
        
        # Insert data
        self.db_manager_test.insert_data(sample_data)
        
        # Export to CSV
        output_file = 'test_output.csv'
        self.db_manager_test.export_to_csv(output_file)
        
        # Verify CSV export
        self.assertTrue(os.path.exists(output_file))
        with open(output_file, 'r') as file:
            content = file.read()
            self.assertIn('John Doe', content)
            self.assertIn('Jane Smith', content)
        self.logger.info("test_export_to_csv: CSV export test passed.")

    def test_export_to_json(self):
        # Sample data to insert
        sample_data = [
            ('John Doe', 'john@example.com', '12345', 'Manager'),
            ('Jane Smith', 'jane@example.com', '67890', 'Developer')
        ]
        
        # Insert data
        self.db_manager_test.insert_data(sample_data)
        
        # Export to JSON
        output_file = 'test_output.json'
        self.db_manager_test.export_to_json(output_file)
        
        # Verify JSON export
        self.assertTrue(os.path.exists(output_file))
        with open(output_file, 'r') as file:
            content = file.read()
            self.assertIn('John Doe', content)
            self.assertIn('Jane Smith', content)
        self.logger.info("test_export_to_json: JSON export test passed.")

    def tearDown(self):
        # Close the database connection after each test
        self.db_manager_test.close_connection()

        # Delete the test database file after each test
        if os.path.exists('test_sample.db'):
            os.remove('test_sample.db')

        # Delete the output CSV file after each test
        if os.path.exists('test_output.csv'):
            os.remove('test_output.csv')

        # Delete the output json file after each test
        if os.path.exists('test_output.json'):
            os.remove('test_output.json')

        # print dashes for pretty reading output log
        print('-------------------------------------------')
if __name__ == '__main__':
    unittest.main()

