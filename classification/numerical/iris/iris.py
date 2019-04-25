import scipy.sparse
import pandas as pd

if __name__ == '__main__':
    sparse_matrix = scipy.sparse.load_npz('/Users/adnanbajwa/Desktop/sparse_matrix.npz')
    df = pd.DataFrame(sparse_matrix.todense())
    print('debug')