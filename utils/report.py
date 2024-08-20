from utils import fileManager
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ReportGenerator:
    """
    A class to generate a PDF report from CSV and JSON files.
    """
    def __init__(self, csv_file_path, json_file_path, pdf_path):
        """
        Initializes the ReportGenerator with file paths and sets up the PDF canvas.
        
        :param csv_file_path: Path to the CSV file.
        :param json_file_path: Path to the JSON file.
        :param pdf_path: Path where the generated PDF will be saved.
        """
        self.csv_file_path = csv_file_path
        self.json_file_path = json_file_path
        self.pdf_path = pdf_path
        self.file_manager = fileManager.FileManager()

        try:
            self.csv_data = self.file_manager.read_csv(self.csv_file_path)
            self.json_data = self.file_manager.read_json(self.json_file_path)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

        self.pdf_canvas = canvas.Canvas(self.pdf_path, pagesize=letter)
        self.width, self.height = letter

        # Define layout parameters
        self.title_font_size = 16
        self.title_x = self.width / 2 - 50
        self.title_y = self.height - 72
        self.margin = 72
        self.line_height = 20
        self.section_title_font_size = 12
        self.section_title_y_offset = 20
        self.sample_records_limit = 5

    def prepare_pdf(self):
        """
        Prepares the PDF by setting the title.
        """
        try:
            self.pdf_canvas.setFont("Helvetica-Bold", self.title_font_size)
            self.pdf_canvas.drawString(self.title_x, self.title_y, "Data Report")
            # Initialize y_position for the rest of the content
            self.y_position = self.title_y - self.line_height * 2
        except Exception as e:
            print(f"Failed to prepare PDF: {e}")
            raise

    def add_total_records(self):
        """
        Adds the total number of records to the PDF.
        """
        try:
            # Add the heading in bold
            self.pdf_canvas.setFont("Helvetica-Bold", self.section_title_font_size)
            self.pdf_canvas.drawString(self.margin, self.y_position, "Total number of records:")
            
            # Add the number (not bold)
            total_records = len(self.csv_data)
            self.y_position -= self.line_height  # Move y_position down for the number
            self.pdf_canvas.setFont("Helvetica", self.section_title_font_size)
            self.pdf_canvas.drawString(self.margin, self.y_position, str(total_records))
            
            self.y_position -= self.line_height * 2  # Move y_position down for the next section
        except Exception as e:
            print(f"Failed to add total records: {e}")
            raise

    def add_sample_records(self):
        """
        Adds sample records to the PDF.
        """
        try:
            self.pdf_canvas.setFont("Helvetica-Bold", self.section_title_font_size)
            self.pdf_canvas.drawString(self.margin, self.y_position, "Sample Records:")
            self.y_position -= self.line_height  # Move y_position down before adding sample records
            self.pdf_canvas.setFont("Helvetica", self.section_title_font_size)  # Reset font for sample records
            
            for row in self.csv_data[:self.sample_records_limit]:  # Limit to 5 records
                row_text = ', '.join(f"{k}: {v}" for k, v in row.items())
                self.pdf_canvas.drawString(self.margin, self.y_position, row_text)
                self.y_position -= self.line_height
            self.y_position -= self.line_height  # Additional space after sample records
        except Exception as e:
            print(f"Failed to add sample records: {e}")
            raise

    def add_unique_companies(self):
        """
        Adds the number of unique companies to the PDF.
        """
        try:
            companies = set()
            for record in self.csv_data:
                email = record.get('email', '')
                company = email.split('@')[-1].split('.')[0]  # Extract company from email
                companies.add(company)
            
            num_companies = len(companies)
            
            # Add the heading in bold
            self.pdf_canvas.setFont("Helvetica-Bold", self.section_title_font_size)
            self.pdf_canvas.drawString(self.margin, self.y_position, "Number of unique companies:")
            
            # Add the number (not bold)
            self.y_position -= self.line_height  # Move y_position down for the number
            self.pdf_canvas.setFont("Helvetica", self.section_title_font_size)
            self.pdf_canvas.drawString(self.margin, self.y_position, str(num_companies))

        except Exception as e:
            print(f"Failed to add unique companies: {e}")
            raise

    def add_title_counts(self):
        """
        Adds the counts of each title to the PDF.
        """
        try:
            title_counts = {}
            for record in self.csv_data:
                title = record.get('title', '')
                title_counts[title] = title_counts.get(title, 0) + 1
            
            self.y_position -= self.section_title_y_offset*2  # Move y_position down before adding "Number of each title:"
            self.pdf_canvas.setFont("Helvetica-Bold", self.section_title_font_size)
            self.pdf_canvas.drawString(self.margin, self.y_position, "Number of each title:")
            self.y_position -= self.section_title_y_offset  # Move y_position down before adding title counts
            self.pdf_canvas.setFont("Helvetica", self.section_title_font_size)  # Reset font for title counts
            
            for title, count in title_counts.items():
                self.pdf_canvas.drawString(self.margin, self.y_position, f"{title}: {count}")
                self.y_position -= self.line_height
        except Exception as e:
            print(f"Failed to add title counts: {e}")
            raise

    def save_report(self):
        """
        Saves the generated PDF report and prints a confirmation message.
        """
        try:
            self.pdf_canvas.save()
            print(f"Report saved as {self.pdf_path}")
        except Exception as e:
            print(f"Failed to save report: {e}")
            raise

    def generate_report(self):
        """
        Generates the complete report by calling all necessary methods.
        """
        try:
            self.prepare_pdf()
            self.add_total_records()
            self.add_sample_records()
            self.add_unique_companies()
            self.add_title_counts()
            self.save_report()
        except Exception as e:
            print(f"Failed to generate report: {e}")
 