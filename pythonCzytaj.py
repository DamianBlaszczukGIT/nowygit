import csv
import os

def sum_time_if_a(path):
    Atime = 0

    with open(path, "r", newline='') as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            row_0 = row[0]
            row_0 = row_0.strip()

            if row_0 == 'A':
                timeString = row[2]
                timeString = timeString.replace('s', '').strip()
                Atime += int(timeString)

    return Atime


def sum_if_a_on_paths(path_list):
    sumTime = 0

    for path in path_list:
        if os.path.exists(path):
            sumTime += sum_time_if_a(path)
        else:
            print(f"Brak ścieżki: {path}")

    return sumTime