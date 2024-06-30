# Mengimpor modul 're' untuk menggunakan fungsi regex
import re

# String yang berisi pesan dengan beberapa alamat email
s = 'A message from snehil@google.com to palak@google.com about meeting @2PM'

# Menggunakan re.findall untuk mencari semua pola yang sesuai dengan format email dalam string 's'
# Pola '\S+@\S+' mencari substring yang mengandung karakter non-spasi diikuti oleh '@' dan diikuti lagi oleh karakter non-spasi
emails = re.findall('\S+@\S+', s)

# Mencetak daftar email yang ditemukan
print(emails)