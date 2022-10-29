from email.quoprimime import quote
import random
import csv
from math import log10

N_SIMULATION = 1000
N_YEARS = 50

roi_table = []
output = {}
avg_rate = 1

if (__name__ == '__main__'):

    # Read in the table of annual growth rates
    with open('../data.csv', newline='') as file:
        # Skip first line (headers)
        next(file, None)

        reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            roi_table.append(round(row[0] + row[1], 4))
  
    with open('out.txt', mode='w') as file:
        for s in range(N_SIMULATION):
            cur_rate = 1

            for y in range(N_YEARS):
                # each year get a random return rate
                roi = roi_table[random.randint(0, len(roi_table)-1)]
                cur_rate *= roi
                file.write(str(round(cur_rate, 4)) + ' ')

            file.write('\n')

            

    