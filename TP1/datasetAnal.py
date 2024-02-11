import sys
import os

def athleteDistr(data):
    len_data = len(data)
    range_15_19 = 0
    range_20_24 = 0
    range_25_29 = 0
    range_30_34 = 0
    range_35_39 = 0
    range_40_45 = 0

    for row in data:
        if 15 <= int(row['idade']) <= 19:
            range_15_19 +=1
        if 20 <= int(row['idade']) <= 24:
            range_20_24 +=1
        if 25 <= int(row['idade']) <= 29:
            range_25_29 +=1
        if 30 <= int(row['idade']) <= 34:
            range_30_34 +=1
        if 35 <= int(row['idade']) <= 39:
            range_35_39 +=1
        if 40 <= int(row['idade']) <= 45:
            range_40_45 +=1

    print()
    print("Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ")
    print("Percentagem de atletas entre 15 e 19 anos: {:.2f}%".format((range_15_19 / len_data) * 100))
    print("Percentagem de atletas entre 20 e 24 anos: {:.2f}%".format((range_20_24 / len_data) * 100))
    print("Percentagem de atletas entre 25 e 29 anos: {:.2f}%".format((range_25_29 / len_data) * 100))
    print("Percentagem de atletas entre 30 e 34 anos: {:.2f}%".format((range_30_34 / len_data) * 100))
    print("Percentagem de atletas entre 35 e 39 anos: {:.2f}%".format((range_35_39 / len_data) * 100))
    print("Percentagem de atletas entre 40 e 45 anos: {:.2f}%".format((range_40_45 / len_data) * 100))


def ableAthletes(data):
    total = len(data)
    able = 0
    unable = 0
    for row in data:
        if row['resultado'] == 'true' :
            able +=1
        else :
            unable +=1
    print("Percentagem de atletas aptos: " + str((able/total)*100) + "%")
    print("Percentagem de atletas inaptos: " + str((unable/total)*100) + "%")


# Define the function to order sports alphabetically
def sportsOrdered(data):
    sports = []
    for row in data:
        modalidade = row['modalidade']
        if modalidade not in sports:
            sports.append(modalidade)
    
    sports.sort()
    return sports


def printSports(ordered_sports):
    i = 1
    print("Lista de desportos ordenada alfabeticamente: ")
    
    for row  in ordered_sports:
        print(str(i) + " - " + row)
        i += 1

def main():
    current_directory = os.path.dirname(__file__)
    csv_file_path = os.path.join(current_directory, 'emd.csv')

    # Define an empty list to store the dictionaries
    data = []

    # Open the CSV file and read its contents
    with open('emd.csv', 'r', encoding='utf-8') as file:
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

    # Call the sportsOrdered function
    ordered_sports = sportsOrdered(data)

    # Print the ordered list of sports
    printSports(ordered_sports)

    print()
    # Call able athlets function
    ableAthletes(data)

    # Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos)
    athleteDistr(data)

    print()

if __name__ == "__main__":
    main()
