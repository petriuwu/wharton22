import random
import csv

table = []
N_SIMULATION = 100
N_YEARS = 100
N_GRACE = 5
REQUIRED_RET = 5000
INITIAL_AMT = 20000

if (__name__ == '__main__'):
    with open('../data.csv', newline='') as file:
        # Skip first line (headers)
        next(file, None)
        table = list(csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC))

    cnt = 0

    with open('output.txt', mode='w') as file:
        for s in range(N_SIMULATION):
            money = INITIAL_AMT
            avg_ret = 0
            avg_div = 0
            failed = False 
            data = []

            for yr in range(N_YEARS):
                if money <= 0:
                    failed = True
                    break

                idx = random.randint(0, len(table)-1)
                
                # stock return rate and dividend rate
                ret_rate = table[idx][0]
                div_rate = table[idx][1]

                dividends = div_rate * money
                money *= ret_rate + div_rate

                if yr >= N_GRACE:
                    money -= REQUIRED_RET

                avg_ret += ret_rate
                avg_div += div_rate

                data.append(money)
                file.write(str(round(money, 4)) + ' ')

            if not failed:
                cnt += 1

            file.write('\n')

    print("Sucess: " + str(cnt) + '/' + str(N_SIMULATION))

    

                
