import random
table = []
N_SIMULATION = 100
N_YEARS = 100
REQUIRED_RET = 5000
INITIAL_AMT = 20000

if (__name__ == '__main__'):
    with open('input.txt', mode='r') as file:
        for line in file:
            table.append([float(x) for x in line.split()])

    print(len(table))

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
                    # print('Failed')
                    failed = True
                    break

                idx = random.randint(0, len(table)-1)
                
                # stock return rate and dividend rate
                ret_rate = table[idx][0]
                div_rate = table[idx][1]

                dividends = div_rate * money
                money *= ret_rate + div_rate

                if yr > 4:
                    money -= REQUIRED_RET

                avg_ret += ret_rate
                avg_div += div_rate

                data.append(money)

                # print('Year       \t' + str(i+1))
                # print('Initial    \t' + str(money))
                # print('Growth Rate\t' + str(ret_rate))
                # print('Div Rate   \t' + str(div_rate))
                # print('Dividend   \t' + str(dividends))
                # print('Deficit    \t' + str(REQUIRED_RET - dividends))
                # print('New        \t' + str(money))
                # print('\n')

            if not failed:
                print("Average Return Rate: " + str(avg_ret / N_YEARS))
                print("Average Div Rate: " + str(avg_div / N_YEARS))
                cnt += 1

            for val in data:
                file.write(str(round(val, 3)) + ' ')
            file.write('\n')

    print("Sucess: " + str(cnt) + '/' + str(N_SIMULATION))

    

                
