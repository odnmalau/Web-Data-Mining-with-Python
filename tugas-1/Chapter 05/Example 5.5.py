# Mengimpor modul urlopen dari urllib.request untuk membuka URL dan modul BeautifulSoup untuk parsing HTML
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Membuka URL YouTube dan membaca kontennya
html = urlopen('https://www.youtube.com/watch?v=-5B858LWJD0')

# Parsing konten halaman menggunakan BeautifulSoup
bs = BeautifulSoup(html, 'html.parser')

# Mendefinisikan URL video YouTube
video_url = "https://www.youtube.com/watch?v=-5B858LWJD0"

# Membuat sesi permintaan HTTP
session = requests.Session()

# Mengirim permintaan GET ke URL video
response = session.get(video_url)

# Mencari semua elemen meta dalam halaman
bs.find_all("meta")