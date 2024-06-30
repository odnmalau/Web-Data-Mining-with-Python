# Mengimpor modul nltk
import nltk

# Mengunduh model 'punkt' untuk tokenisasi kalimat
nltk.download('punkt')

# Mengunduh model 'averaged_perceptron_tagger' untuk penandaan bagian dari ucapan (POS tagging)
nltk.download('averaged_perceptron_tagger')

# Mengimpor fungsi sent_tokenize dari nltk.tokenize untuk memisahkan teks menjadi kalimat
from nltk.tokenize import sent_tokenize

# Mendefinisikan teks yang akan di-tokenisasi
txt = "I love watching movies. I and my friends love eating popcorn and snacks while watching Movie."

# Menggunakan fungsi sent_tokenize untuk memisahkan teks menjadi kalimat
tokenized = sent_tokenize(txt)

# Mencetak hasil tokenisasi kalimat
print(tokenized)