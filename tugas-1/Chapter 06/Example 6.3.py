# Mengimpor modul nltk
import nltk

# Mengimpor fungsi word_tokenize dan sent_tokenize dari nltk.tokenize untuk memisahkan teks menjadi kata dan kalimat
from nltk.tokenize import word_tokenize, sent_tokenize

# Mendefinisikan teks yang akan di-tokenisasi
txt = "I love watching movies. Me and my friends love eating popcorn and snacks while watching the movie."

# Menggunakan fungsi sent_tokenize untuk memisahkan teks menjadi kalimat
tokenized = sent_tokenize(txt)

# Loop melalui setiap kalimat yang telah di-tokenisasi
for i in tokenized:
    # Menggunakan fungsi word_tokenize untuk memisahkan kalimat menjadi kata
    wordsList = nltk.word_tokenize(i)
    # Menggunakan fungsi pos_tag untuk melakukan POS tagging pada daftar kata
    tagged = nltk.pos_tag(wordsList)
    # Mencetak hasil POS tagging
    print(tagged)