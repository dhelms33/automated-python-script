import pytest
from unittest.mock import mock_open, patch
from script import CSVReader, Compare  # Replace 'your_module' with the actual module name

@patch('builtins.open', new_callable=mock_open, read_data='Display Name,Gross Transaction Amount\nJohn Doe,100\nJane Smith,200\n')
def test_csv_reader(mock_file):
    reader = CSVReader('fake_path.csv')
    data = reader.read()
    expected = [
        {'Display Name': 'John Doe', 'Gross Transaction Amount': '100'},
        {'Display Name': 'Jane Smith', 'Gross Transaction Amount': '200'}
    ]
    assert data == expected
    mock_file.assert_called_once_with('fake_path.csv', 'r')

@pytest.fixture
def sample_data():
    return (
        [
            {'Display Name': 'John Doe', 'Gross Transaction Amount': '100'},
            {'Display Name': 'Jane Smith', 'Gross Transaction Amount': '200'}
        ],
        [
            {'Donor': 'John Doe', 'Row Checksum': '100'},
            {'Donor': 'Jane Smith', 'Row Checksum': '200'}
        ]
    )

@patch('builtins.print')
def test_compare(sample_data, mock_print):
    data1, data2 = sample_data
    comparer = Compare(data1, data2)
    comparer._check_field("Display Name", "Gross Transaction Amount")
    mock_print.assert_called_once_with("The records for the fields are the same.")
