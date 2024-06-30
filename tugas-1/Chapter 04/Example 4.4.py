# Mendefinisikan variabel 'number' dengan nilai 32
number = 32

# Mendefinisikan variabel 'running' dengan nilai True untuk mengontrol loop
running = True

# Memulai loop while yang akan terus berjalan selama 'running' bernilai True
while running:
    # Meminta pengguna untuk memasukkan sebuah bilangan bulat dan mengonversinya menjadi tipe integer
    choice = int(input('Enter an integer: '))
    
    # Memeriksa apakah nilai 'choice' sama dengan 'number'
    if choice == number:
        # Jika kondisi benar, cetak pesan selamat dan informasi bahwa tidak ada hadiah
        print("Congratulations, you guessed it.")
        print('but you do not win any prizes!')
        # Mengubah nilai 'running' menjadi False untuk menghentikan loop
        running = False
    # Memeriksa apakah nilai 'choice' kurang dari 'number'
    elif choice < number:
        # Jika kondisi benar, cetak pesan bahwa angka yang ditebak terlalu rendah
        print('No, it is a little higher than that')
    # Jika tidak ada kondisi di atas yang terpenuhi, berarti 'choice' lebih besar dari 'number'
    else:
        # Cetak pesan bahwa angka yang ditebak terlalu tinggi
        print('No, it is a little lower than that')
# Blok else ini akan dijalankan ketika loop while selesai
else:
    print('The while loop is over.')

# Cetak pesan 'Done' setelah selesai memeriksa semua kondisi
print('Done')