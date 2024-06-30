# Mendefinisikan fungsi 'greater' yang membandingkan dua angka dan mengembalikan yang lebih besar
def greater(a, b):
    if a > b:
        return a
    else:
        return b

# Mendefinisikan variabel 'x' dengan nilai 5 dan 'y' dengan nilai 7
x = 5
y = 7

# Memanggil fungsi 'greater' dengan 'x' dan 'y' sebagai argumen dan menyimpan hasilnya dalam variabel 'max'
max = greater(x, y)

# Mencetak nilai 'max' dengan pesan bahwa itu adalah angka yang lebih besar
print(max, 'is greater')

# Memanggil fungsi 'greater' dengan 3 dan 4 sebagai argumen dan mencetak hasilnya dengan pesan bahwa itu adalah angka yang lebih besar
print(greater(3, 4), 'is greater')