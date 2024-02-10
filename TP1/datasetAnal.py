import sys
import os

current_directory = os.path.dirname(__file__)
csv_file_path = os.path.join(current_directory, 'emd.csv')


# Define an empty list to store the dictionaries
data = []

# Open the CSV file and read its contents
with open('emd.csv', 'r') as file:
    # Read the header line to get column names
    headers = file.readline().strip().split(',')

    # Iterate over each line in the file
    for line in file:
        # Split the line into values
        values = line.strip().split(',')

        # Create a dictionary for the current row
        row_dict = dict(zip(headers, values))

        # Append the row (dictionary) to the data list
        data.append(row_dict)

