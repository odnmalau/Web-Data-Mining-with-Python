# Mendefinisikan variabel 'number' dengan nilai 32
number = 32

# Memulai loop for yang akan berjalan sebanyak 5 kali
for i in [1, 2, 3, 4, 5]:
    # Meminta pengguna untuk memasukkan sebuah bilangan bulat dan mengonversinya menjadi tipe integer
    guess = int(input('Enter an integer: '))
    
    # Memeriksa apakah nilai 'guess' sama dengan 'number'
    if guess == number:
        # Jika kondisi benar, cetak pesan selamat dan informasi bahwa tidak ada hadiah
        print("Congratulations, you guessed it.")
        print('but you do not win any prizes!')
        # Menghentikan loop dengan pernyataan break
        break
    # Memeriksa apakah nilai 'guess' kurang dari 'number'
    elif guess < number:
        # Jika kondisi benar, cetak pesan bahwa angka yang ditebak terlalu rendah
        print('No, it is a little higher than that')
    # Jika tidak ada kondisi di atas yang terpenuhi, berarti 'guess' lebih besar dari 'number'
    else:
        # Cetak pesan bahwa angka yang ditebak terlalu tinggi
        print('No, it is a little lower than that')
# Blok else ini akan dijalankan ketika loop for selesai tanpa break
else:
    print('The for loop is over.')

# Cetak pesan 'Done' setelah selesai memeriksa semua kondisi
print('Done')