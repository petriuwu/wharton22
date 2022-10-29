from matplotlib import scale
import matplotlib.pyplot as plt
from math import log10
size = 100

avg = 0
n_sim = 0

if (__name__ == '__main__'):
    plt.locator_params(nbins=10)
    
    with open('out.txt', mode='r') as file:
        for line in file:
            list = [float(val) for val in line.strip().split(' ')]
            plt.plot(list)
            
            avg += (list[len(list)-1] ** (1/(len(list))))
            n_sim += 1

    plt.xscale('linear')
    plt.yscale('log')
    plt.show()

    print(avg / n_sim)

    