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

class Compare:
    """Class to compare fields from two CSV data sets."""
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def _check_field(self, field1, field2):
        """General method to check if the values of fields are the same in both data sets."""
        try:
            data1_values = {(row['Display Name'], row['Gross Transaction Amount']) for row in self.data1}
            data2_values = {(row['Donor'], row['(Do Not Modify) Row Checksum']) for row in self.data2}
            
            only_in_data1 = data1_values - data2_values
            only_in_data2 = data2_values - data1_values

            if not only_in_data1 and not only_in_data2:
                print(f"The records for the fields are the same.")
            else:
                print(f"The records for the fields are different.")
                if only_in_data1:
                    print(f"Records only in data1:")
                    for item in only_in_data1:
                        print(item)
                if only_in_data2:
                    print(f"Records only in data2:")
                    for item in only_in_data2:
                        print(item)
        except KeyError as e:
            print(f"KeyError: {e} - Please check if the column name exists in the CSV files.")

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
    comparer._check_field("Display Name", "Gross Transaction Amount")

if __name__ == '__main__':
    main()
