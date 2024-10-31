import argparse
import os
import random

import pythonCzytaj

def create_paths(months, days, times):
    day_names = {
        'pn': 'poniedzialek',
        'wt': 'wtorek',
        'sr': 'sroda',
        'cz': 'czwartek',
        'pt': 'piatek',
        'sb': 'sobota',
        'nd': 'niedziela'
    }

    time_names = {
        'r': 'rano',
        'w': 'wieczorem'
    }

    paths = []
    counter = 0
    for month, days in zip(months, days):
        for day in days:
            day_full = day_names.get(day)

            time_full = time_names.get(times[counter])
            counter += 1

            path = f"{month.capitalize()}/{day_full}/{time_full}/dane.csv"

            paths.append(path)

    return paths


def write_to_file(path):
    x = random.choice(['A', 'B', 'C'])
    y = random.randint(0, 1000)
    z = random.randint(0, 1000)

    with open(path, 'w') as file:
        file.write("Model; Wynik; Czas;\n")
        file.write(f"{x} ; {y} ; {z}s;")
        file.flush()  #Ensure that file is updated/created before we read from it(in case both --t and --o are on)


def create_files_on_paths(paths):
    for path in paths:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        write_to_file(path)


def get_weekdays(a, day_list):
    days = a.split("-")
    return day_list[day_list.index(days[0]) : day_list.index(days[1]) + 1 if len(days) > 1 else day_list.index(days[0]) + 1]


def run_args(arguments):
    months_list = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]
    days_list = ["pn", "wt", "sr", "cz", "pt", "sb", "nd"]

    months = list(filter(lambda m: m in months_list, arguments.items))

    days_temp = arguments.items[len(months) : 2 * len(months)]
    days = list(map(lambda x: get_weekdays(x, days_list), days_temp))

    days_length = sum(map(len, days))
    times = arguments.items[2 * len(months) : ]
    times.extend(['r'] * (days_length - len(times)))

    paths = create_paths(months, days, times)

    if arguments.t:
        create_files_on_paths(paths)

    if arguments.o:
        print(pythonCzytaj.sum_if_a_on_paths(paths))


def main():
    parser = argparse.ArgumentParser(
        description="Program do tworzenia lub odczytu plików na ścieżkach zadanych przez parametry odpalenia programu."
                    "W przypadku tworzenia pliku -> gdy na zadanej ścieżce już istnieje plik, to jest on nadpisywany."
                    "W przypadku odczytu -> gdy na zadanej ścieżce nie ma pliku to wyświetlany jest odpowiedni komunikat."
    )

    parser.add_argument(
        "items",
        nargs="*",
        help="Lista miesięcy, dni i pór dnia (np. styczen luty pn-cz sb r w)"
             "Nazwy miesięcy powinny zaczynac sie z malej litery i nie zawierac polskich znaków."
             "Argumenty odpowiadajace koljnym dniom tygodnia: pn, wt, sr, cz, pt, sb, nd."
    )

    # Adding optional arguments
    parser.add_argument(
        "--t",
        action="store_true",
        help="Flaga czy tworzymy pliki, domyślnie przyjmuje wartość false (Uwaga: gdy próbujemy jednocześnie utworzyć i przeczytać pliki, prgoram jedynie je utworzy)"
    )

    parser.add_argument(
        "--o",
        action="store_true",
        help="Flaga czy odczytujemy z plików, domyślnie przyjmuje wartość false (Uwaga: gdy próbujemy jednocześnie utworzyć i przeczytać pliki, prgoram jedynie je utworzy)"
    )

    args = parser.parse_args()

    run_args(args)


if __name__ == '__main__':
    main()