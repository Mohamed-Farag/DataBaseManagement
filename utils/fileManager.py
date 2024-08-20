import csv
import json

class FileManager:
    def read_csv(self, csv_file):
        """
        Read data from the CSV file.
        :param csv_file: Path to the CSV file
        :return: Data as a list of dictionaries
        """
        try:
            with open(csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            return data
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return []

    def read_json(self, json_file):
        """
        Read data from the JSON file.
        :param json_file: Path to the JSON file
        :return: Data as a list of dictionaries
        """
        try:
            with open(json_file, mode='r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return []
