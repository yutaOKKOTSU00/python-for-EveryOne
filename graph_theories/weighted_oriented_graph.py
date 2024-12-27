# CELL 5: Weighted oriented graph adjacency matrix

def Initialisation2(sommets):
    matrice = []
    
    for i in range(sommets):
        ligne = []
        for j in range(sommets):
            nombre = -5
            while nombre < 0:
                nombre = int(input(f"A[{i}, {j}]: "))
            ligne.append(nombre)
        matrice.append(ligne)
    return matrice