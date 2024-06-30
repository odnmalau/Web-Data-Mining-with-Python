# Mendefinisikan variabel 'number' dengan nilai 32
number = 32

# Meminta pengguna untuk memasukkan sebuah bilangan bulat dan mengonversinya menjadi tipe integer
choice = int(input('Enter an integer: '))

# Memeriksa apakah nilai 'choice' sama dengan 'number'
if choice == number:
    # Jika kondisi benar, cetak pesan selamat dan informasi bahwa tidak ada hadiah
    print("Congratulations, you guessed it.")
    print('but you do not win any prizes!')
# Memeriksa apakah nilai 'choice' kurang dari 'number'
elif choice < number:
    # Jika kondisi benar, cetak pesan bahwa angka yang ditebak terlalu rendah
    print('No, it is a little higher than that')
# Jika tidak ada kondisi di atas yang terpenuhi, berarti 'choice' lebih besar dari 'number'
else:
    # Cetak pesan bahwa angka yang ditebak terlalu tinggi
    print('No, it is a little lower than that')

# Cetak pesan 'Done' setelah selesai memeriksa semua kondisi
print('Done')