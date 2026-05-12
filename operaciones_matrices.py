def sumar_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        return None
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

def hadamard_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def kronecker(A, B):
    filas_A, cols_A = len(A), len(A[0])
    filas_B, cols_B = len(B), len(B[0])
    C = [[0 for _ in range(cols_A * cols_B)] for _ in range(filas_A * filas_B)]
    for i in range(filas_A):
        for j in range(cols_A):
            for k in range(filas_B):
                for l in range(cols_B):
                    C[i * filas_B + k][j * cols_B + l] = A[i][j] * B[k][l]
    return C