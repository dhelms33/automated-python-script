import csv
from os import name

class CSVReader:
    """Class to read CSV files."""
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        """Read the CSV file and return the data as a list of dictionaries."""
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

class Compare:
    """Class to compare fields from two CSV data sets."""
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2


    def _check_field(self, field):
        """General method to check if the values of a field are the same in both data sets."""
        values1 = {(row['Display Name'], row['gross transaction amount'],) for row in self.data1}
        values2 = {(row['donor'], row['row checksum'],) for row in self.data2}
        
        if values1 == values2:
            print(f"The records for the field '{field}' are the same.")
        else:
            print(f"The records for the field '{field}' are different.")

def main():
    # Initialize CSVReader objects
    csv1 = CSVReader('PS-23-002 CSV Classy Report.csv')
    csv2 = CSVReader('PS-23-002 CSV FE Report.csv')
    
    # Read CSV data
    data1 = csv1.read()
    data2 = csv2.read()

    # Initialize Compare object
    comparer = Compare(data1, data2)

    # Check specific fields
    comparer._check_field("Display Name")

if __name__ == '__main__':
    main()
