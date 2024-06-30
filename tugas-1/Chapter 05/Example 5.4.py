# Mengimpor modul urlopen dari urllib.request untuk membuka URL dan modul BeautifulSoup untuk parsing HTML
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Membuka URL Wikipedia dan membaca kontennya
html = urlopen('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')

# Parsing konten halaman menggunakan BeautifulSoup
bs = BeautifulSoup(html, 'html.parser')

# Menemukan semua elemen gambar (img) yang memiliki atribut 'src' yang mengandung '.jpg'
images = bs.find_all('img', {'src': re.compile('.jpg')})

# Loop melalui setiap elemen gambar dan mencetak atribut 'src' yang berisi URL gambar
for image in images:
    print(image['src'] + '\n')