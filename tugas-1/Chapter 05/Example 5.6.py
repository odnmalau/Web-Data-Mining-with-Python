# Mengimpor modul requests untuk mengirim permintaan HTTP dan modul BeautifulSoup untuk parsing HTML
import requests
from bs4 import BeautifulSoup

# Mendefinisikan URL video YouTube
video_url = "https://www.youtube.com/watch?v=-5B858LWJD0"

# Membuat sesi permintaan HTTP
session = requests.Session()

# Mengirim permintaan GET ke URL video
response = session.get(video_url)

# Parsing konten halaman menggunakan BeautifulSoup
bs = BeautifulSoup(response.text, "html.parser")

# Menemukan dan menyimpan metadata video
name = bs.find("meta", itemprop="name")["content"]
count = bs.find("meta", itemprop="interactionCount")['content']
desc = bs.find("meta", itemprop="description")['content']

# Mencetak metadata video
print("Title of the video is:", name)
print("Number of views are:", count)
print("Description of video is:", desc)