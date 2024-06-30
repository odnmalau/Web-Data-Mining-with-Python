# Mengimpor modul networkx untuk manipulasi grafik
import networkx as nx

# Membaca grafik dari file edgelist
G = nx.read_edgelist("Dataset/facebook_combined.txt")

# Mencetak informasi grafik
print(nx.info(G))