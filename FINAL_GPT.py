import csv

class CSVReader:
    """Class to read CSV files."""
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        """Read the CSV file and return the data as a list of dictionaries."""
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                print(f"Columns in {self.file_path}: {reader.fieldnames}")
                return data
        except FileNotFoundError:
            print(f"FileNotFoundError: The file '{self.file_path}' was not found.")
        except IOError:
            print(f"IOError: There was an issue opening the file '{self.file_path}'.")

class Compare:
    """Class to compare fields from two CSV data sets."""
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def compare_fields(self, field1, field2):
        """Method to compare specified fields from both data sets."""
        try:
            if not self.data1 or not self.data2:
                print("One of the datasets is empty or not properly loaded.")
                return

            data1_values = {(row[field1], row[field2]) for row in self.data1}
            data2_values = {(row[field1], row[field2]) for row in self.data2}
            
            only_in_data1 = data1_values - data2_values
            only_in_data2 = data2_values - data1_values

            if not only_in_data1 and not only_in_data2:
                print(f"The records for fields '{field1}' and '{field2}' are the same.")
            else:
                print(f"The records for fields '{field1}' and '{field2}' are different.")
                if only_in_data1:
                    print(f"Records only in data1:")
                    for item in only_in_data1:
                        print(item)
                if only_in_data2:
                    print(f"Records only in data2:")
                    for item in only_in_data2:
                        print(item)
        except KeyError as e:
            print(f"KeyError: {e} - Please check if the column names '{field1}' and '{field2}' exist in the CSV files.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    # Initialize CSVReader objects
    csv1 = CSVReader('PS-23-002 CSV Classy Report.csv')
    csv2 = CSVReader('PS-23-002 CSV FE Report.csv')
    
    # Read CSV data
    data1 = csv1.read()
    data2 = csv2.read()

    # Ensure that data is properly loaded before comparing
    if data1 is None or data2 is None:
        print("Comparison cannot be performed due to an error in reading the CSV files.")
        return

    # Initialize Compare object
    comparer = Compare(data1, data2)

    # Example fields to compare, can be modified as needed
    field1 = "Display Name"
    field2 = "Gross Transaction Amount"
    comparer.compare_fields(field1, field2)

if __name__ == '__main__':
    main()
