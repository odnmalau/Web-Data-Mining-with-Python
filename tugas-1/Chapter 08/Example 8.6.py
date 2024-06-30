# Mengimpor modul networkx untuk manipulasi grafik
import networkx as nx

# Membuat objek grafik kosong
G = nx.Graph()

# Menambahkan edge dengan atribut 'relation' ke grafik
G.add_edge('A', 'B', relation='Family')
G.add_edge('B', 'C', relation='Friend')
G.add_edge('C', 'F', relation='Extended Family')

# Menggambar grafik dengan label node
nx.draw(G, with_labels=True)

# Mencetak edge dalam grafik
print(G.edges())