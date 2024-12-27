# CELL 3: initialisation and displaying of oriented graph adjacecny matrix

def Initialisation(sommets):
    matrice = []
    
    for i in range(sommets):
        ligne = []
        for j in range(sommets):
            nombre = 5
            while nombre != 0 and nombre != 1:
                nombre = int(input('Matrice[{}, {}]: '.format(i, j)))
            ligne.append(nombre)
        matrice.append(ligne)
        
    return matrice


def Affichage(matrice, sommets, i):
    print('\n',i)
    for ligne in matrice:
        print('\t',ligne)