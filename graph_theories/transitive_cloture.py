# CELL 9: transitive cloture of adjacent matrix
from graph_operations import Unions, Produit

def copy_init(matrix):
    matrix_copy = matrix
    
    return matrix_copy
    
def K_incrementation(k):
    return k+1

def Compare_matrix(matrix1, matrix2):
    if matrix1 == matrix2:
        return 1
    else:
        return 0
    

def transit(matrix, sommets):
    # second N=M, K=2
    matrix_N = copy_init(matrix)
    matrix_k = copy_init(matrix)
    k = 2
    while True:
        # third calcul of M**K
        matrix_k = Produit(matrix_k, matrix, sommets)

        # fourth
        boolean_product = Unions(matrix_N, matrix_k, sommets)

        if Compare_matrix(matrix_N, boolean_product):
            return matrix, matrix_N
            break
        else:
            matrix_N = copy_init(boolean_product)
            k = K_incrementation(k)