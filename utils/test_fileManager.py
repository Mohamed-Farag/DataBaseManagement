import unittest
from unittest.mock import mock_open, patch
from fileManager import FileManager
import json

class TestFileManager(unittest.TestCase):
    # This decorator replaces the open function with a mock object that simulates opening a file with predefined content.
    # Creates a mock object to simulate file operations
    # The read_data argument specifies the content that the file should return when read.
    @patch("builtins.open", new_callable=mock_open, read_data='col1,col2\nval1,val2\nval3,val4\n')
    def test_read_csv(self, mock_open):
        fm = FileManager()
        data = fm.read_csv('fake_path.csv')
        expected_data = [{'col1': 'val1', 'col2': 'val2'}, {'col1': 'val3', 'col2': 'val4'}]
        self.assertEqual(data, expected_data)

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"key1": "value1"}, {"key2": "value2"}]))
    def test_read_json(self, mock_open):
        fm = FileManager()
        data = fm.read_json('fake_path.json')
        expected_data = [{"key1": "value1"}, {"key2": "value2"}]
        self.assertEqual(data, expected_data)

    @patch("builtins.open", new_callable=mock_open)
    def test_read_csv_error(self, mock_open):
        # Simulate an error by raising an IOError
        mock_open.side_effect = IOError("File not found")
        fm = FileManager()
        data = fm.read_csv('fake_path.csv')
        self.assertEqual(data, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_read_json_error(self, mock_open):
        # Simulate an error by raising an IOError
        mock_open.side_effect = IOError("File not found")
        fm = FileManager()
        data = fm.read_json('fake_path.json')
        self.assertEqual(data, [])

if __name__ == "__main__":
    unittest.main()
