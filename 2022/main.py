import numpy as np

N = 4
sc_matric = np.random.randn(4, 4)

degree4nodes = np.sum(sc_matric, 0)


coupling_matrix = np.zeros([N*6, N*6])


# assume X=[x1i,y1i,x2i,y2i,zi,auxiliary_variable,......]
for i in range(N):
    coupling_matrix[i*6+5, i*6] += degree4nodes[i]
    for j in range(N):
        coupling_matrix[i*6+5, j*6] -= sc_matric[i, j]
print(coupling_matrix.shape)
