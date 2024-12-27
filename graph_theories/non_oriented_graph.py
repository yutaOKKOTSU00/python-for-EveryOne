# CELL 4: not oriented graph adjacency matrix
from oriented_graph import Initialisation

def Initialisation1(sommets):
    matrix = Initialisation(sommets)
    for i in range(sommets):
        for j in range(sommets):
            while matrix[i][j] != matrix[j][i]:
                print('\nmatrix[{}][{}] = {} est different de matrix[{}][{}] = {}'.format(i, j, matrix[i][j], j, i, matrix[j][i]))
                print('saisissez 1 pour changer matrix[{}][{}] autrement changer matrix[{}][{}] \n'.format(i, j, j, i)) 
                nombre = int(input('choix'))
                if nombre == 1:
                    matrix[i][j] = int(input(f'matrix[{i}][{j}]'))
                else:
                    matrix[j][i] = int(input(f'matrix[{j}][{i}]'))
    return matrix