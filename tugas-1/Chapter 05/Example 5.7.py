# Mengimpor modul urlopen dari urllib.request untuk membuka URL dan modul BeautifulSoup untuk parsing HTML
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Mendefinisikan dictionary untuk menyimpan hasil
result = {}

# Membuka URL YouTube dan membaca kontennya
html = urlopen('https://www.youtube.com/watch?v=-5B858LWJD0')

# Parsing konten halaman menggunakan BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Mendefinisikan URL video YouTube
video_url = "https://www.youtube.com/watch?v=-5B858LWJD0"

# Membuat sesi permintaan HTTP
session = requests.Session()

# Mengirim permintaan GET ke URL video
response = session.get(video_url)

# Menyimpan metadata video dalam dictionary
result["title"] = soup.find("meta", itemprop="name")['content']
result["views"] = soup.find("meta", itemprop="interactionCount")['content']
result["description"] = soup.find("meta", itemprop="description")['content']
result["date_published"] = soup.find("meta", itemprop="datePublished")['content']
result["duration"] = soup.find("meta", itemprop="duration")['content']

# Mencetak metadata video
for i in result:
    print(i, ":", result[i])
    print("\n")