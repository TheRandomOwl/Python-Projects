import csv

# Import the necessary modules

def readCSV(filename):
    '''
    Read a CSV file and return the average of the values in the second column
    input: filename (str)
    output: average (float)
    '''
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        total = 0
        count = 0
        for row in reader:
            total += float(row[1])
            count += 1
    return total/count

def main():
    readCSV('data.csv')

if __name__ == '__main__':
    main()