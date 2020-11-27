import csv

data = []
def read_csv():
    with open('data/data.csv', 'r') as table:
        reader = csv.DictReader(table)

        for row in reader:
            data.append(row)
        print(data)

if __name__ == '__main__':
    read_csv()
