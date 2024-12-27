from dijkstra_matrice import dijkstra as dj

def Initialisation2(sommets):   # matrice orientée pondérée
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

def Initialisation(sommets):    # matrice orientée non pondérée
    matrice = Initialisation2(sommets)
    
    for i in range(sommets):
        for j in range(sommets):
            while matrice[i][j] != matrice[j][i]:
                print('\nmatrice[{}][{}] = {} est différente de matrice[{}][{}] = {}'.format(i, j, matrice[i][j], j, i, matrice[j][i]))
                print('saisissez 1 pour changer matrice[{}][{}] autrement changer matrice[{}][{}] \n'.format(i, j, j, i)) 
                nombre = int(input('choix'))
                if nombre == 1:
                    matrice[i][j] = int(input(f'matrice[{i}][{j}]'))
                else:
                    matrice[j][i] = int(input(f'matrice[{j}][{i}]'))
    return matrice

def Affichage(matrice, sommets, i):
    print('\n', i)
    for ligne in matrice:
        print('\t', ligne)
        
sommets = int(input('entrez le nombre de sommets: '))
matrice = Initialisation(sommets)
Affichage(matrice, sommets, 'Matrice')
start = int(input('entrez le commencement du graphe (un entier indice du sommet dans la matrice): '))
print("la plus petite distance à partir du sommet", start)
resultat = dj(matrice, start)

# tri
sommets_ordonnes = []
for i in range(len(resultat)):
    sommets_ordonnes.append(resultat[i])    
resultat.sort()
for i in range(len(sommets_ordonnes)):
    print(f'{sommets_ordonnes.index(resultat[i])}:{resultat[i]}')