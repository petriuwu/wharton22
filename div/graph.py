import matplotlib.pyplot as plt

if (__name__ == '__main__'):
    plt.locator_params(nbins=10)
    
    with open('output.txt', mode='r') as file:
        for line in file:
            list = [float(val) for val in line.strip().split(' ')]
            plt.plot(list)


    plt.xscale('linear')
    plt.yscale('log')
    plt.show()