# Mengimpor modul os untuk berinteraksi dengan sistem operasi
import os

# Mengimpor modul subprocess untuk menjalankan proses eksternal
import subprocess

# Fungsi untuk menjalankan semua file Python dalam direktori tertentu
def run_all_python_files():
    # Mendapatkan direktori kerja saat ini
    directory = os.getcwd()
    
    # Daftar nama folder yang akan diproses
    for foldername in ["Chapter 01", "Chapter 03", "Chapter 04", "Chapter 05", "Chapter 06", "Chapter 07", "Chapter 08"]:
        # Membentuk path lengkap ke folder
        folderpath = os.path.join(directory, foldername)
        
        # Memeriksa apakah path tersebut adalah direktori
        if os.path.isdir(folderpath):
            # Melakukan iterasi melalui semua file dalam direktori
            for filename in os.listdir(folderpath):
                # Memeriksa apakah file tersebut memiliki ekstensi .py
                if filename.endswith(".py"):
                    # Membentuk path lengkap ke file
                    filepath = os.path.join(folderpath, filename)
                    try:
                        # Menjalankan file Python menggunakan subprocess.run
                        subprocess.run(["python", filepath], check=True)
                    except subprocess.CalledProcessError as e:
                        # Menangani error jika eksekusi file Python gagal
                        print(f"Error executing {filepath}: {e}")

# Memanggil fungsi utama jika skrip dijalankan secara langsung
if __name__ == "__main__":
    run_all_python_files()
