import numpy as np


def main():
    '''
    COS method
    '''   
    r, sigma, S0, K, T = 0.04, 0.3, 100, 110, 1
    
    a = np.log(S0/K) + r*T - 12 * np.sqrt(sigma*sigma*T)
    b = np.log(S0/K) + r*T + 12 * np.sqrt(sigma*sigma*T)

    print(a,b)


main()
