import numpy as np

# robust, lasso
def l1_norm(x):
    x_norm = np.abs(x)
    x_norm = np.sum(x_norm)
    return x_norm

# laplace
def l2_norm(x):
    x_norm = x*x
    x_norm = np.sum(x_norm)
    x_norm = np.sqart(x_norm)
    return x_norm

def l2_norm_np(x):
    return np.linalg.norm(x)

print(l1_norm([1,2,6,4]))

# subtraction: distance between two vectors

# angles between two vectors *ONLY in L2 Norm*
def angle(x,y):
    v = np.inner(x,y)/ (l2_norm(x)*l2_norm(y))
    theta = np.arcos(v)
    return theta

# Orthogonal Projection = |x|cos(theta)
