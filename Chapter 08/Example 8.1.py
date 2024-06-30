# Mengimpor modul networkx untuk manipulasi grafik
import networkx as nx

# Membuat objek grafik kosong
G = nx.Graph()

# Menambahkan edge ke grafik
G.add_edge('A', 'B')
G.add_edge('B', 'C')

# Mencetak node dan edge dalam grafik
print(G.nodes())
print(G.edges())