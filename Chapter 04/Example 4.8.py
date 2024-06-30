# Mendefinisikan fungsi 'greater' yang membandingkan dua angka dan mencetak yang lebih besar
def greater(a, b):
    if a > b:
        print(a, 'is greater than', b)
    else:
        print(b, 'is greater than', a)

# Mendefinisikan variabel 'x' dengan nilai 5 dan 'y' dengan nilai 7
x = 5
y = 7

# Memanggil fungsi 'greater' dengan 'x' dan 'y' sebagai argumen
greater(x, y)

# Memanggil fungsi 'greater' dengan 3 dan 4 sebagai argumen
greater(3, 4)