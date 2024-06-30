# Mengimpor modul requests untuk mengirim permintaan HTTP dan modul BeautifulSoup untuk parsing HTML
import requests
from bs4 import BeautifulSoup

# Mendefinisikan URL dari situs web yang akan diambil gambarnya
url = 'https://rubikscode.net/'

# Mengirim permintaan GET ke URL dan menyimpan responsnya
r = requests.get(url)

# Parsing konten halaman menggunakan BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# Menemukan semua elemen gambar (img) dalam halaman
images = soup.find_all('img')

# Inisialisasi variabel untuk menghitung jumlah gambar yang diunduh
fl = 0

# Loop melalui setiap elemen gambar
for image in images:
    # Mendapatkan URL gambar dari atribut 'src'
    link = image['src']
    # Menambah nilai counter gambar
    fl = int(fl) + 1
    # Membuka file baru untuk menyimpan gambar
    with open('file' + str(fl) + '.jpg', 'wb') as f:
        # Mengirim permintaan GET ke URL gambar
        in = requests.get(link)
        # Menulis konten gambar ke file
        f.write(in.content)