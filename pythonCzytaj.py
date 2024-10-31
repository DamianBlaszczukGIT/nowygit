import csv
import os

def sumTimeIfA(path):
    Atime = 0

    with open(path, "r", newline='') as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            if row[0] == 'A':
                timeString = row[2]
                timeString.replace('s', '').strip()
                Atime += int(timeString)

    return Atime


def sumATime(path_list):
    sumTime = 0

    for path in path_list:
        if os.path.exists(path):
            sumTime += sumTimeIfA(path)
        else:
            print("Brak ścieżki")

    return sumTime