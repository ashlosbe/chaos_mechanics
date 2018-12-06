import numpy as np
from matplotlib import pyplot as plt

def bifurcation_diagram(r_num,j_num):
    log_map = [[2/3 for i in range(j_num)] for r in range(r_num)]
    for r in range(r_num):
        for j in range(j_num-1):
            log_map[r][j+1] = (3+r/r_num)*log_map[r][j]*(1-log_map[r][j])
        r_vals = [3+r/1000 for j in range(j_num-1000)]
        plt.scatter(r_vals,log_map[r][1000:],s=0.00001,c='b')
    plt.show()
    
bifurcation_diagram(1000,2000)
