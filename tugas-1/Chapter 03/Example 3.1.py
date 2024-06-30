# Dataset transaksi yang berisi daftar item yang dibeli bersama
dataset = [
    ["Milk", "Eggs", "Bread", "Butter"],
    ["Milk", "Butter", "Eggs", "Apple"],
    ["Milk", "Eggs", "Bread"],
    ["Bread", "Butter"],
    ["Eggs", "Apple"],
]

# Mengimpor modul pandas untuk manipulasi data
import pandas as pd

# Mengimpor TransactionEncoder dari mlxtend.preprocessing untuk mengubah dataset transaksi menjadi format yang sesuai
from mlxtend.preprocessing import TransactionEncoder

# Membuat instance dari TransactionEncoder
te = TransactionEncoder()

# Menyesuaikan dan mengubah dataset transaksi menjadi array boolean
# Setiap baris mewakili transaksi, dan setiap kolom mewakili item
te_array = te.fit(dataset).transform(dataset)

# Mengubah array boolean menjadi DataFrame pandas
# Kolom DataFrame adalah nama item, dan nilai boolean menunjukkan apakah item tersebut ada dalam transaksi
df = pd.DataFrame(te_array, columns=te.columns_)

# Mengimpor fungsi apriori dari mlxtend.frequent_patterns untuk menemukan itemset yang sering muncul
from mlxtend.frequent_patterns import apriori

# Menemukan itemset yang sering muncul dengan minimum support 0.01
# Parameter use_colnames=True memastikan bahwa nama item digunakan sebagai kolom
frequent_itemsets_ap = apriori(df, min_support=0.01, use_colnames=True)

# Mengimpor fungsi association_rules dari mlxtend.frequent_patterns untuk menghasilkan aturan asosiasi
from mlxtend.frequent_patterns import association_rules

# Menghasilkan aturan asosiasi dari itemset yang sering muncul
# Menggunakan metrik 'confidence' dengan ambang batas minimum 0.8
rules_ap = association_rules(frequent_itemsets_ap, metric="confidence", min_threshold=0.8)