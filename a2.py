import numpy as np

def main():
    n = 444075
    f = np.loadtxt('txTripletsCounts.txt', dtype=int)
    M = np.empty([n,n])

    for l in f:
        sender = l[0]
        receiver = l[1]
        num_trans = l[2]
        M[sender, receiver] = num_trans

main()
