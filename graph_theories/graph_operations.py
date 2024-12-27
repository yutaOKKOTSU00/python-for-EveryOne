# operation sur la matrice d'adjacence

def Unions(matrice1, matrice2, sommets):
    matrice_union = []
    
    for i in range(sommets):
        ligne = []
        for j in range(sommets):
            if matrice1[i][j] == matrice2[i][j]:
                ligne.append(matrice2[i][j])
            else:
                ligne.append(1)
        matrice_union.append(ligne)
        
    return matrice_union


def Intersection(matrice1, matrice2, sommets):
    matrice_inters = []
    
    for i in range(sommets):
        ligne = []
        for j in range(sommets):
            if matrice1[i][j] == matrice2[i][j]:
                ligne.append(matrice2[i][j])
            else:
                ligne.append(0)
        matrice_inters.append(ligne)
        
    return matrice_inters


def Complement(matrice, sommets):
    complement = []
    
    for i in range(sommets):
        ligne = []
        for j in range(sommets):        
            if matrice[i][j]  == 1:
                ligne.append(0)
            else:
                ligne.append(1)
        complement.append(ligne)
        
    return complement


def Inverse(matrice, sommets):
    inverse = []
    
    for i in range(sommets):
        ligne = []
        for j in range(sommets):
            ligne.append(0)
        inverse.append(ligne)
        
    for i in range(sommets):
        for j in range(sommets):
            inverse[i][j] = matrice[j][i]
            
    return inverse


def Produit(matrice1, matrice2, sommets):
    produit = []
    
    for i in range(sommets):
        ligne = []
        for j in range(sommets):
            ligne.append(0)
        produit.append(ligne)
        
    for i in range(sommets):
        for j in range(sommets):
            for k in range(sommets):
                produit[i][j] += matrice1[i][k]*matrice2[k][j]
                if produit[i][j]>1:
                    produit[i][j] = 1
   
    return produit