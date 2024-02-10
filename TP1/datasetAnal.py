import sys
import os

current_directory = os.path.dirname(__file__)
csv_file_path = os.path.join(current_directory, 'emd.csv')

with open(csv_file_path, 'r') as file:
    for linha in file:
        print(linha)
