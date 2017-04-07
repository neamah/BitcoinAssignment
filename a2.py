import numpy as np
from scipy.sparse import *
from sklearn.utils.extmath import randomized_svd
from sklearn.decomposition import TruncatedSVD

def main():
    n = 444075
    f = np.loadtxt('txTripletsCounts.txt', dtype=int)
    M = coo_matrix((f[:,2], (f[:,0], f[:,1])), shape=(n, n))

    svd = TruncatedSVD(n_components=11)
    X = svd.fit_transform(M)
    print X
    print X.shape
    print svd.explained_variance_ratio_


main()
