import graph_operations as go
import graph_propertises as gp
import list_graph_representation as gl
import non_oriented_graph as gon
import non_oriented_weighted_graph as gnw
import oriented_graph as gop
import transitive_cloture as gt
import tuples_graph_representation as gr
import weighted_oriented_graph as gow


# tuples_graph_representation
print('tuples', gr.G)


# list_graph_representation
print('relations',gl.adjacency_dict(gr.G))


sommets = int(input('entrez le nombe de sommets'))


# non_oriented_graph
print('\nveuillez saisir une matrice de graph non oriente')
matrix = gon.Initialisation1(sommets)
gop.Affichage(matrix, sommets, ' matrice non orientee')


# weighted_oriented_graph
print('\nveuillez saisir une matrice de graph oriente pondere')
matrice1 = gow.Initialisation2(sommets)
gop.Affichage(matrice1, sommets, 'matrice oriente pondere ')


# non_oriented_weighted_graph
print('\nveuillez saisir une matrice de graph non oriente pondere')
matrix = gnw.Initialisation3(sommets)
gop.Affichage(matrix, sommets, ' matrice non oriente pondere')


# graph_operations
print('\nveuillez saisir deux matrices qui subiront des operations matricielles')
print('matrice 1')
matrice1 = gop.Initialisation(sommets)
gop.Affichage(matrice1, sommets, 'matrice 1')

print('matrice 2')
matrice2 = gop.Initialisation(sommets)
gop.Affichage(matrice2, sommets, 'matrice 2')

matrice_union = go.Unions(matrice1, matrice2, sommets)
gop.Affichage(matrice_union, sommets, 'union')

matrice_inters = go.Intersection(matrice1, matrice2, sommets)
gop.Affichage(matrice_inters, sommets, 'intersection')

complement1 = go.Complement(matrice1, sommets)
gop.Affichage(complement1, sommets, 'complement de la matrice1')

complement2 = go.Complement(matrice2, sommets)
gop.Affichage(complement2, sommets, 'complement de la matrice 2')

inverse1 = go.Inverse(matrice1, sommets)
gop.Affichage(inverse1, sommets, 'inverse de la matrice 1')

inverse2 = go.Inverse(matrice2, sommets)
gop.Affichage(inverse2, sommets, 'inverse de la matrice 2')

produit = go.Produit(matrice1, matrice2, sommets)
gop.Affichage(produit, sommets, 'produit')


# properties
# matrice 1
gop.Affichage(matrice1, sommets, 'propriete de la matrice 2')

if gp.Totalite(matrice1, sommets):
    print('la matrice est totalite')
else:
    print('la matrice n est pas totalite')

if gp.Determinisme(matrice1, sommets):
    print('la matrice est Determinisme')
else:
    print('la matrice n est pas Determinisme')
    
if gp.Surjectivite(matrice1, sommets):
    print('la matrice est Surjectivite')
else:
    print('la matrice n est pas Surjectivite')

if gp.Injectivite(matrice1, sommets):
    print('la matrice est Injectivite')
else:
    print('la matrice n est pas Injectivite')

if gp.Application(matrice1, sommets):
    print('la matrice est Application')
else:
    print('la matrice n est pas Application')

if gp.Application_bijective(matrice1, sommets):
    print('la matrice est Application bijective')
else:
    print('la matrice n est pas Application bijective')

# matrice 2
gop.Affichage(matrice2, sommets, 'propriete de la matrice 2')

if gp.Totalite(matrice2, sommets):
    print('la matrice est totalite')
else:
    print('la matrice n est pas totalite')

if gp.Determinisme(matrice2, sommets):
    print('la matrice est Determinisme')
else:
    print('la matrice n est pas Determinisme')
    
if gp.Surjectivite(matrice2, sommets):
    print('la matrice est Surjectivite')
else:
    print('la matrice n est pas Surjectivite')

if gp.Injectivite(matrice2, sommets):
    print('la matrice est Injectivite')
else:
    print('la matrice n est pas Injectivite')

if gp.Application(matrice2, sommets):
    print('la matrice est Application')
else:
    print('la matrice n est pas Application')

if gp.Application_bijective(matrice2, sommets):
    print('la matrice est Application bijective')
else:
    print('la matrice n est pas Application bijective')


# transitive cloture
# matrice 1
matrix, matrix_N =  gt.transit(matrice1, sommets)
gop.Affichage(matrix, sommets, 'Matrice 1')
gop.Affichage(matrix_N, sommets, 'fermeture transitive:')

# matrice 2
matrix, matrix_N =  gt.transit(matrice2, sommets)
gop.Affichage(matrix, sommets, 'Matrice 2')
gop.Affichage(matrix_N, sommets, 'fermeture transitive:')