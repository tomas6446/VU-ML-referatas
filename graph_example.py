import networkx as nx
import matplotlib.pyplot as plt

# Sukuriamas tuščias grafas
G = nx.Graph()

# Pridedami mazgai - draugai
G.add_node("Alice")
G.add_node("Bob")
G.add_node("Charlie")
G.add_node("Dave")
G.add_node("Eve")
G.add_node("Frank")

# Pridedamos briaunos - draugystės
G.add_edge("Alice", "Bob")
G.add_edge("Alice", "Charlie")
G.add_edge("Alice", "Dave")
G.add_edge("Bob", "Charlie")
G.add_edge("Bob", "Dave")
G.add_edge("Charlie", "Dave")
G.add_edge("Charlie", "Eve")
G.add_edge("Dave", "Eve")
G.add_edge("Eve", "Frank")

# Pavaizduojamas grafas
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=16)
plt.show()
