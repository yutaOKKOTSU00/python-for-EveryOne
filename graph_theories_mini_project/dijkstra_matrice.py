from graph import graph

def dijkstra(graphe, depart):
    n = len(graphe)  # nombre de sommets
    distances = [float('inf')] * n  # crée une liste avec n éléments tous initialisés à l'infini
    distances[depart] = 0  # initialisation du sommet de départ à 0
    visites = [False] * n  # création d'une liste avec n éléments tous initialisés à False pour savoir si les sommets sont visités ou non
    
    for _ in range(n):  # utilisation du caractère underscore si on n'a pas besoin de connaître le nombre d'itérations
        u = min_distance(distances, visites)    # sommet actuel
        visites[u] = True   
        
        for v in range(n):
            if graphe[u][v] > 0 and not visites[v]:  # vérifier les conditions et mettre à jour les distances si plus petites que l'actuelle
                if distances[u] + graphe[u][v] < distances[v]:
                    distances[v] = distances[u] + graphe[u][v]
                    
    return distances

def min_distance(distances, visites):  # donner l'index du sommet non visite avec la plus courte distance 
    distance_min = float('inf')
    index_min = 0
    
    for i in range(len(distances)):
        if distances[i] < distance_min and not visites[i]:
            distance_min = distances[i]
            index_min = i
            
    return index_min

debut = 0
print("la plus petite distance à partir du sommet", debut)
resultat = dijkstra(graph, debut)

for i in range(len(resultat)):
    print(f'{i}:{resultat[i]}')