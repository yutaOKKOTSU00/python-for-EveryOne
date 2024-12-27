from graph import graphe
import heapq  # module pour la manipulation de structures de donnees
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graphe, depart):
    file_priorite = [(0, depart)]  # liste de tuple contenant un noeud et sa  distance
    distances = {sommet: float('infinity') for sommet in graphe} # liste de distances initializes a infini
    distances[depart] = 0 # mettre la distance du noeud de depart a 0

    G = nx.Graph(graphe)

    while file_priorite:  # tant que la file de priorite n'est pas vide
        distance_courante, sommet_courant = heapq.heappop(file_priorite)  # renvoie le plus petit element de la liste et le supprime de celle ci

        if distance_courante > distances[sommet_courant]:
            continue

        for voisin, poids in graphe[sommet_courant].items():
            distance = distance_courante + poids
            if distance < distances[voisin]:
                distances[voisin] = distance
                heapq.heappush(file_priorite, (distance, voisin))  # mise a jour de la liste de distance
                G.add_edge(sommet_courant, voisin, weight=poids)  # dessiner l'arc entre le sommet et son voisin

    return distances, G

start_vertex = 'A'
resultat, graphe_visualisation = dijkstra(graphe, start_vertex)
temps_minimum = 0

for sommet in graphe:
    if resultat[sommet] > temps_minimum:
        temps_minimum = resultat[sommet]  # temps minimum pour parcourir tout le graphe

# Visualiser le graphe
pos = nx.spring_layout(graphe_visualisation)
labels_arrete = nx.get_edge_attributes(graphe_visualisation, 'weight')
nx.draw(graphe_visualisation, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10)
nx.draw_networkx_edge_labels(graphe_visualisation, pos, edge_labels=labels_arrete)
plt.title(f"Algorithme de Dijkstra - Distances les plus courtes depuis {start_vertex}")

# Afficher le résultat sous le graphe
plt.figtext(0.5, 0.02, f"plus courts Chemins depuis {start_vertex}: {resultat}", ha='center', va='center', fontsize=10)

# Afficher le graphe et le résultat
plt.show()