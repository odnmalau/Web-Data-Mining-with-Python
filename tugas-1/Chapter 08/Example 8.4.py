# Mengimpor modul networkx untuk manipulasi grafik
import networkx as nx

# Membuat objek grafik terarah (directed graph)
G = nx.DiGraph()

# Menambahkan edge ke grafik terarah
G.add_edge('B', 'A')
G.add_edge('B', 'C')
G.add_edge('C', 'F')
G.add_edge('C', 'E')
G.add_edge('E', 'D')
G.add_edge('G', 'F')

# Menggambar grafik dengan label node
nx.draw(G, with_labels=True)