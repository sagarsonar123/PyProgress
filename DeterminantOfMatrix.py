import numpy as np
A=np.array([5,10,5])
B=np.array([0,7,-15])
C=np.array([-5,0,0])
vAdd=(np.add(A,B,C))
print(np.add(B,C))
print(vAdd)
print(np.linalg.norm(vAdd))
