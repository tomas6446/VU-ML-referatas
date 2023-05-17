import networkx as nx
import matplotlib.pyplot as plt

# RDF triplai
triples = [
    ("Vilnius", "yra sostine", "Lietuva"),
    ("Lietuva", "valiuta", "EUR"),
    ("Vilnius", "regionas", "Vilniaus apskritis"),
    ("Lietuva", "gyventoju skaicius", "2860002"),
    ("Vilnius", "gyventoju skaicius", "591632")
]

# Sukuriamas tuščias NetworkX grafas
G = nx.DiGraph()

# Pridedami grafai ir briaunos iš triplų sąrašo
for triple in triples:
    subject, predicate, obj = triple
    G.add_node(subject)
    G.add_node(obj)
    G.add_edge(subject, obj, label=predicate)

# Grafo vaizdavimas
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=1000)
nx.draw_networkx_labels(G, pos, font_size=14, font_weight="bold")

nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True)

nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'), font_color='red')
plt.axis('off')
plt.show()