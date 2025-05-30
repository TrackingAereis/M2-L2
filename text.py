# Kode ini memungkinkan kita untuk membaca seluruh isi file teks.
f = open('coba.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()