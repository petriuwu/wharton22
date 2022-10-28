import random
from math import log10
N_SIMULATION = 1000
N_YEARS = 50

roi_table = []
output = {}
avg_rate = 0

if (__name__ == '__main__'):

    # Read in the table of annual growth rates
    with open('input2.txt', mode='r') as file:
        for line in file:
            roi_table.append(float(line))
          
    avg = 0
    with open('output.txt', mode='w') as file:
        for s in range(N_SIMULATION):
            cur_rate = 1

            for y in range(N_YEARS):
                roi = roi_table[random.randint(0, len(roi_table)-1)]
                cur_rate *= roi
                file.write(str(round(cur_rate, 3)) + ' ')

            file.write('\n')

            

    