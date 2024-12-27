graph = [
  #  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U
  
    [0, 3, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    #A
    [3, 0, 0, 0, 12, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #B
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    #C
    [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    #D
    [0, 12, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   #E
    [0, 11, 5, 6, 4, 0, 3, 0, 5, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   #F
    [8, 0, 0, 0, 0, 3, 0, 1, 0, 6, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0],   #G
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    #H
    [0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    #I
    [0, 0, 0, 0, 0, 9, 6, 4, 0, 0, 8, 8, 0, 1, 0, 6, 4, 0, 12, 0, 0],   #J
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],   #K
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],   #L
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 2, 0, 0],   #M
    [0, 0, 0, 0, 0, 0, 13, 0, 0, 1, 0, 0, 10, 0, 11, 0, 0, 0, 6, 0, 0], #N
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0],   #O
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0],    #P
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 0],    #Q
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 9, 3, 0],    #R
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 2, 6, 0, 0, 0, 9, 0, 0, 5],   #S
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2],    #T
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 0]     #U
]


# graphe est un dictionaire a l'interieur duquel chaque sommet de la matrice est la cle d'un autre dictionaire qui aura pour cle tous les sommets lies a ce sommet et comme valeurs les distances entre ces derniers

sommets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
graphe = {}
for i in range(len(graph)):
    dict = {}
    for j in range(len(graph)):
        if graph[i][j] != 0:
            dict[sommets[j]]=graph[i][j]
    graphe[sommets[i]] = dict

#print(graphe)