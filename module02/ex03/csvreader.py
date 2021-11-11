import csv

#? opens, reads, and parses a CSV file

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        pass

    def __enter__(filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_index = 0
            for row in csv_reader:
                if line_index == 0:
                    print(f'column -> {"".join(row)}')
                    line_index += 1
                else:
                    i = 0
                    while (row[i]):
                        print(f'row[{i}] -> {row[i]}\n')
                        i += 1
        print(f'-------> line_index : {line_index}\n')             

    def __exit__():
        pass
