# Mengimpor modul BeautifulSoup untuk parsing HTML dan requests untuk mengirim permintaan HTTP
from bs4 import BeautifulSoup
import requests

# Membuat sesi permintaan HTTP
session = requests.Session()

# Mendefinisikan payload untuk login
payload = {'_username': '[YOUR_USERNAME]', 
           '_password': '[YOUR_PASSWORD]'
          }

# Mengirim permintaan POST untuk login
s = session.post("https://www.chess.com/login_check", data=payload)

# Mengirim permintaan GET untuk mengambil konten dari halaman setelah login
s = session.get('https://www.chess.com/today')

# Parsing konten halaman menggunakan BeautifulSoup
soup = BeautifulSoup(s.text, 'html.parser')