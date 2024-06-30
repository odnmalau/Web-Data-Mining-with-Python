# Mengimpor modul networkx untuk manipulasi grafik
import networkx as nx

# Membuat objek grafik kosong
G = nx.Graph()

# Menambahkan beberapa edge ke grafik
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'E'), ('E', 'D'), ('C', 'F'), ('G', 'F')])

# Mencetak node dan edge dalam grafik
print(G.nodes())
print(G.edges())

# Menggambar grafik dengan label node
nx.draw(G, with_labels=True)