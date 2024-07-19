import csv

class CSVReader:
    """Class to read CSV files."""
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        """Read the CSV file and return the data as a list of dictionaries."""
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            # Print column names for debugging
            print(f"Columns in {self.file_path}: {reader.fieldnames}")
            return data

class CSVWriter:
    """Class to write CSV files."""
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data, fieldnames):
        """Write the data to a CSV file."""
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

def merge_data(data1, data2):
    """Merge the data from two CSV files into a unified format."""
    merged_data = []

    for row in data1:
        merged_data.append({
            'Name': row['Display Name'],
            'Amount': row['Gross Transaction Amount']
        })

    for row in data2:
        merged_data.append({
            'Name': row['Donor'],
            'Amount': row['(Do Not Modify) Row Checksum']
        })

    return merged_data

def main():
    # Initialize CSVReader objects
    csv1 = CSVReader('PS-23-002 CSV Classy Report.csv')
    csv2 = CSVReader('PS-23-002 CSV FE Report.csv')
    
    # Read CSV data
    data1 = csv1.read()
    data2 = csv2.read()

    # Merge the data
    merged_data = merge_data(data1, data2)

    # Define the fieldnames for the merged CSV
    fieldnames = ['Name', 'Amount']

    # Initialize CSVWriter object
    merged_csv = CSVWriter('merged_data.csv')

    # Write the merged data to a new CSV file
    merged_csv.write(merged_data, fieldnames)

if __name__ == '__main__':
    main()
