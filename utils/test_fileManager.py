import unittest
from unittest.mock import patch, mock_open
from fileManager import FileManager

class TestFileManager(unittest.TestCase):
    
    # This decorator replaces the open function with a mock object that simulates opening a file with predefined content.
    # Creates a mock object to simulate file operations
    # The read_data argument specifies the content that the file should return when read.
    @patch("builtins.open", new_callable=mock_open, read_data="col1,col2\nval1,val2\nval3,val4")
    def test_read_csv_success(self, mock_file):
        fm = FileManager()
        expected_data = [{'col1': 'val1', 'col2': 'val2'}, {'col1': 'val3', 'col2': 'val4'}]
        result = fm.read_csv("dummy.csv")
        self.assertEqual(result, expected_data)

    @patch("builtins.open", new_callable=mock_open)
    def test_read_csv_exception(self, mock_file):
        mock_file.side_effect = Exception("File not found")
        fm = FileManager()
        with self.assertLogs(level='ERROR') as log:
            result = fm.read_csv("dummy.csv")
            self.assertIn("Error reading CSV file: File not found", log.output[0])
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data='{"key1": "value1", "key2": "value2"}')
    def test_read_json_success(self, mock_file):
        fm = FileManager()
        expected_data = {"key1": "value1", "key2": "value2"}
        result = fm.read_json("dummy.json")
        self.assertEqual(result, expected_data)

    @patch("builtins.open", new_callable=mock_open)
    def test_read_json_exception(self, mock_file):
        mock_file.side_effect = Exception("File not found")
        fm = FileManager()
        with self.assertLogs(level='ERROR') as log:
            result = fm.read_json("dummy.json")
            self.assertIn("Error reading JSON file: File not found", log.output[0])
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
