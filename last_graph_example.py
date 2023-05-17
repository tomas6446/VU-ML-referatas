import networkx as nx
import matplotlib.pyplot as plt

# Sukuriamas naujas grafas
G = nx.DiGraph()

# Pridedamos viršūnės
G.add_node('LeonardoDicaprio', type='actor')
G.add_node('Samuel L. Jackson', type='actor')
G.add_node('Inception', type='movie')
G.add_node('Django Unchained', type='movie')
G.add_node('Pulp Fiction', type='movie')
G.add_node('Quentin Tarantino', type='director')
G.add_node('Interstellar', type='movie')
G.add_node('Christopher Nolan', type='director')
G.add_node('Best Music', type='category')
G.add_node('Best Director', type='category')
G.add_node('Best Picture', type='category')
G.add_node('Oscar', type='award')

# Pridedamos briaunos
G.add_edge('LeonardoDicaprio', 'Inception', relation='filmed in')
G.add_edge('LeonardoDicaprio', 'Django Unchained', relation='filmed in')
G.add_edge('Samuel L. Jackson', 'Django Unchained', relation='filmed in')
G.add_edge('Samuel L. Jackson', 'Pulp Fiction', relation='filmed in')
G.add_edge('Quentin Tarantino', 'Pulp Fiction', relation='directed')
G.add_edge('Christopher Nolan', 'Inception', relation='directed')
G.add_edge('Christopher Nolan', 'Interstellar', relation='directed')
G.add_edge('Interstellar', 'Best Music', relation='nominated')
G.add_edge('Interstellar', 'Best Director', relation='nominated')
G.add_edge('Interstellar', 'Oscar', relation='got')
G.add_edge('Oscar', 'Best Music', relation='category')
G.add_edge('Oscar', 'Best Director', relation='category')
G.add_edge('Oscar', 'Best Picture', relation='category')

# Nuspalviname viršūnes pagal jų tipus
node_colors = {'actor': 'blue', 'director': 'red', 'movie': 'green', 'category': 'orange', 'award': 'yellow'}
colors = [node_colors[G.nodes[node]['type']] for node in G.nodes()]

# Nubraižome grafo vaizdą su etikečių pavadinimais
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=1300, node_color=colors)
nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G.edges[u, v]['relation'] for u, v in G.edges()}, font_size=10, font_family='sans-serif')

plt.axis('off')
plt.show()
