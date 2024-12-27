# CELL 8: adjacency matrix properties

def Totalite(matrice, sommets):  # au moins  un 1 par ligne
    T=1
    
    for i in range(sommets):
        ligne = 0
        for j in range(sommets):
            ligne += matrice[i][j]
        if ligne < 1:
            T = 0
            
    return T  


def Determinisme(matrice, sommets):  # au plus un 1 par ligne
    T=1
    
    for i in range(sommets):
        ligne = 0
        for j in range(sommets):
            ligne += matrice[i][j]
        if ligne > 1:
            T = 0
            
    return T  


def Surjectivite(matrice, sommets):  #au moins un 1 par colonne
    T=1
    
    for i in range(sommets):
        colone = 0
        for j in range(sommets):
            colone += matrice[j][i]
        if colone < 1:
            T = 0
            
    return T


def Injectivite(matrice, sommets):  # au plus un 1 par colonne
    T = 1
    
    for i in range(sommets):
        colone = 0
        for j in range(sommets):
            colone += matrice[j][i]
        if colone > 1:
            T = 0
            
    return T


def Application(matrice, sommets):  # exactement un 1 par ligne
    T = 1
    
    for i in range(sommets):
        ligne = 0
        for j in range(sommets):
            ligne += matrice[i][j]
        if ligne != 1:
            T = 0
            
    return T


def Application_bijective(matrice, sommets):  # exactement un 1 par ligne et par colonne
    T = 1
    
    for i in range(sommets):
        colone = 0
        for j in range(sommets):
            colone += matrice[j][i]
        if colone != 1:
            T = 0
    if not(Application(matrice, sommets)):
        T = 0
        
    return T