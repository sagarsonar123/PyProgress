import numpy as np
from numpy import linalg as LA
cov=np.matrix([[2.0, 0.8], [0.8, 0.6]])
eigenvalue, eigenvector= LA.eig(cov)
print(eigenvalue, eigenvector)