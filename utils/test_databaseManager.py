import unittest
from unittest.mock import patch, MagicMock, mock_open
import csv
import json
from databaseManager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    @patch('sqlite3.connect')
    def setUp(self, mock_connect):
        # Mock the sqlite3.connect method to return a mock connection object
        self.mock_conn = MagicMock()
        mock_connect.return_value = self.mock_conn
        # Initialize the DatabaseManager with the mock connection
        self.db_manager = DatabaseManager('test_db.sqlite')

    def test_create_connection(self):
        # Test that the connection is created and a cursor is obtained
        self.assertIsNotNone(self.db_manager.conn)
        self.mock_conn.cursor.assert_called_once()

    def test_create_table(self):
        # Test that the create_table method executes the correct SQL query
        self.db_manager.create_table()
        self.mock_conn.cursor().execute.assert_called_once()
        self.mock_conn.cursor().execute.assert_called_with('''
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                zip_code TEXT NOT NULL,
                title TEXT NOT NULL
            )
        ''')

    def test_insert_data(self):
        # Test that the insert_data method inserts data correctly
        data = [('John Doe', 'john@example.com', '12345', 'Developer')]
        self.db_manager.insert_data(data)
        self.mock_conn.cursor().executemany.assert_called_once_with('''
            INSERT INTO data (name, email, zip_code, title)
            VALUES (?, ?, ?, ?)
        ''', data)
        self.mock_conn.commit.assert_called_once()

    @patch('builtins.open', new_callable=mock_open)
    def test_export_to_csv(self, mock_open):
        # Mock the cursor's fetchall and description methods
        cursor = self.mock_conn.cursor()
        cursor.fetchall.return_value = [(1, 'John Doe', 'john@example.com', '12345', 'Developer')]
        cursor.description = [('id',), ('name',), ('email',), ('zip_code',), ('title',)]
        
        # Test that the export_to_csv method writes the correct data to a CSV file
        self.db_manager.export_to_csv('output.csv')
        
        mock_open.assert_called_once_with('output.csv', 'w', newline='')
        handle = mock_open()
        handle.write.assert_called()
        writer = csv.writer(handle())
        writer.writerow.assert_called_once_with(['id', 'name', 'email', 'zip_code', 'title'])
        writer.writerows.assert_called_once_with([(1, 'John Doe', 'john@example.com', '12345', 'Developer')])

    @patch('builtins.open', new_callable=mock_open)
    def test_export_to_json(self, mock_open):
        # Mock the cursor's fetchall and description methods
        cursor = self.mock_conn.cursor()
        cursor.fetchall.return_value = [(1, 'John Doe', 'john@example.com', '12345', 'Developer')]
        cursor.description = [('id',), ('name',), ('email',), ('zip_code',), ('title',)]
        
        # Test that the export_to_json method writes the correct data to a JSON file
        self.db_manager.export_to_json('output.json')
        
        mock_open.assert_called_once_with('output.json', 'w')
        handle = mock_open()
        handle.write.assert_called()
        json.dump.assert_called_once_with(
            [{'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'zip_code': '12345', 'title': 'Developer'}],
            handle(),
            indent=4
        )

    def tearDown(self):
        # Close the database connection after each test
        self.db_manager.close_connection()
        self.mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
