import numpy as np

def matrix_factorization(R, P, Q, K=2, steps=5000, alpha=0.0002, beta=0.02, tol=0.001):
    n, m = R.shape
    Q = Q.T
    for _ in range(steps):
        for i in range(n):
            for j in range(m):
                if R[i][j] > 0:
                    eij = R[i][j] - np.dot(P[i,:], Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = np.dot(P, Q)
        e = 0
        for i in range(n):
            for j in range(m):
                if R[i][j] > 0:
                    e = e + (R[i][j] - np.dot(P[i,:], Q[:,j])) ** 2
                    for k in xrange(K):
                        e = e + (beta/2) * (P[i][k] ** 2 + Q[k][j] ** 2) # total error
        if e < tol:
            break
    return P, Q.T

R = np.array([ [ 1, 2, 3, 0 ],
               [ 4, 0, 5, 6 ],
               [ 7, 8, 0, 9 ]]) # user 5
n, m = R.shape
# n = row
#m = column
K = 2 # latent variable
P = np.random.rand(n, K)
Q = np.random.rand(m, K)
P, Q = matrix_factorization(R, P, Q, K)
Rhat = np.dot(P, Q.T)
print(Rhat)