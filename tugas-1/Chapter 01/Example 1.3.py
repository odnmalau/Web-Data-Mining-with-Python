# Import modul untuk menangani URL dan error
import urllib.request, urllib.parse, urllib.error

# Membuka URL yang diberikan dan membaca isinya
f = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Loop melalui setiap baris dalam file yang dibuka
for line in f:
    # Decode setiap baris dari bytes ke string dan hapus spasi di awal/akhir baris
    print(line.decode().strip())