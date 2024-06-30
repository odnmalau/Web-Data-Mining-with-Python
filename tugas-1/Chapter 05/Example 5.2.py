# Mengimpor modul requests untuk mengirim permintaan HTTP dan modul BeautifulSoup untuk parsing HTML
import requests
from bs4 import BeautifulSoup

# Mendefinisikan URL dari situs web yang akan diambil gambarnya
url = 'https://rubikscode.net/'

# Mengirim permintaan GET ke URL dan menyimpan responsnya
ur = requests.get(url)

# Parsing konten halaman menggunakan BeautifulSoup
soup = BeautifulSoup(ur.text, 'html.parser')

# Menemukan semua elemen gambar (img) dalam halaman
images = soup.find_all('img')

# Loop melalui setiap elemen gambar dan mencetak atribut 'src' yang berisi URL gambar
for image in images:
    print(image['src'])