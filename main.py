# use package

# Numpy
import numpy as np

x = np.array([[1,2,3], [4,5,6]])
print("x:\n{}".format(x))

# sciPy

from scipy import sparse

# Create a 2D array with a diagonal of ones, and zeros everywhere are
e = np.eye(4)
print("NumPy array:\n{}".format(e))

# convert the numpy array to a SciPy matrix in CSR format
sparse_mt = sparse.csr_matrix(e)
print('\nSciPy Sparse CSR matrix:\n{}'.format(sparse_mt))

# Create Coo Matrix
dt = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((dt, (row_indices, col_indices)))
print('COO representation:\n{}'.format(eye_coo))