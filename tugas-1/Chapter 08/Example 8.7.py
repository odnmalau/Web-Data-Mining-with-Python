# Mengimpor modul networkx untuk manipulasi grafik
import networkx as nx

# Membuat objek grafik kosong
G = nx.Graph()

# Menambahkan edge dengan atribut 'weight' dan 'relation' ke grafik
G.add_edge('A', 'B', weight=6, relation='family')
G.add_edge('B', 'C', weight=13, relation='friend')

# Menambahkan node dengan atribut 'role' ke grafik
G.add_node('A', role='Director')
G.add_node('B', role='Coordinator')
G.add_node('C', role='Computer Operator')

# Mencetak node dalam grafik
print(G.nodes())

# Mencetak node beserta atributnya dalam grafik
print(G.nodes(data=True))

# Menggambar grafik dengan label node
nx.draw(G, with_labels=True)