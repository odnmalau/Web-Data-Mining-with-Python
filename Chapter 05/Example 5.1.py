# Mengimpor modul builtwith untuk mendeteksi teknologi yang digunakan oleh sebuah situs web
import builtwith

# Menggunakan fungsi parse dari builtwith untuk menganalisis situs web Yahoo
res = builtwith.parse('https://yahoo.com')

# Mencetak hasil analisis yang menunjukkan teknologi yang digunakan oleh situs web
print(res)