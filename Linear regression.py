                                        # LINEAR REGRESSION


import numpy as np
X=np.matrix([[1.0, 4.0], [1.0, 4.5], [1.0, 5.0], [1.0, 5.5], [1.0, 6.0], [1.0, 6.5], [1.0, 7.0]])
Y=np.matrix([[33], [42], [45], [51], [53], [61], [62]])

Xt=np.transpose(X)
print("\nDimensions of X transpose are ", Xt.shape)

XtX= Xt*X

print ("\nThe dimensions of X'X are ", XtX.shape )
XtX_inv= np.linalg.inv(XtX)
print ("\nThe dimensions of inv(X'X) are ", np.shape (XtX_inv))

XtY=Xt*Y


#Coefficient matrix B=  XtX_inv * XtY


B= XtX_inv * XtY
print (B)