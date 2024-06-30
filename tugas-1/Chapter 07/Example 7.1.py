# Mengimpor modul matplotlib.pyplot untuk visualisasi dan networkx untuk manipulasi grafik
import matplotlib.pyplot as plt
import networkx as nx

# Mengimpor algoritma Girvan-Newman dari networkx.algorithms.community.centrality
from networkx.algorithms.community.centrality import girvan_newman

# Membuat grafik klub karate menggunakan fungsi bawaan NetworkX
G = nx.karate_club_graph()

# Menggunakan algoritma Girvan-Newman untuk mendeteksi komunitas dalam grafik
communities = girvan_newman(G)

# Inisialisasi daftar untuk menyimpan grup node
node_groups = []

# Mendapatkan komunitas pertama yang terdeteksi oleh algoritma
for com in next(communities):
    node_groups.append(list(com))

# Mencetak grup node yang terdeteksi
print(node_groups)

# Inisialisasi daftar untuk menyimpan warna node
color_map = []

# Menetapkan warna untuk setiap node berdasarkan komunitasnya
for node in G:
    if node in node_groups[0]:
        color_map.append('blue')
    else:
        color_map.append('green')

# Menggambar grafik dengan warna node yang telah ditetapkan
nx.draw(G, node_color=color_map, with_labels=True)
plt.show()