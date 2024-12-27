import heapq
from graph import graphe

def dijkstra_avec_chemin(graphe, noeud_depart, noeud_arrivee):
    # File de priorité pour contenir (distance, noeud)
    file_priorite = []
    heapq.heappush(file_priorite, (0, noeud_depart))
    
    # Dictionnaire des distances pour contenir la distance la plus courte à chaque noeud
    distances = {noeud: float('inf') for noeud in graphe}
    distances[noeud_depart] = 0
    
    # Dictionnaire des prédécesseurs pour reconstruire le chemin
    predecesseurs = {noeud: None for noeud in graphe}
    
    while file_priorite:
        distance_courante, noeud_courant = heapq.heappop(file_priorite)
        
        # Si nous atteignons le noeud d'arrivée, nous pouvons arrêter
        if noeud_courant == noeud_arrivee:
            break
        
        # Les noeuds ne peuvent être traités qu'une seule fois
        if distance_courante > distances[noeud_courant]:
            continue
        
        for voisin, poids in graphe[noeud_courant].items():  # Changement ici pour dict de dicts
            distance = distance_courante + poids
            
            # Considérer ce nouveau chemin seulement s'il est meilleur
            if distance < distances[voisin]:
                distances[voisin] = distance
                predecesseurs[voisin] = noeud_courant
                heapq.heappush(file_priorite, (distance, voisin))
    
    # Reconstruire le chemin le plus court
    chemin = []
    etape_courante = noeud_arrivee
    while etape_courante is not None:
        chemin.append(etape_courante)
        etape_courante = predecesseurs[etape_courante]
    
    chemin.reverse()  # Inverser le chemin pour l'obtenir du départ à l'arrivée
    
    return distances[noeud_arrivee], chemin, predecesseurs


depart = 'A'
arrivee = 'U'
distance, chemin, predecesseurs = dijkstra_avec_chemin(graphe, depart, arrivee)

print("Distance la plus courte :", distance)
print("Chemin emprunté :", " -> ".join(chemin))
#print(predecesseurs)