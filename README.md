# Project ML-terapan
# Keterangan proyek
Dataset yang digunakan pada proyek ini adalah data harga mobil. 

# Problem statment
Dari dataset tersebut maka pertanyaan bisnis yang diajukan adalah:
1. Tipe dan model mobil apa yang paling banyak diminati ?
2. Tipe dan model mobil apa yang memiliki harga tinggi ?
3. Faktor apa yang mempengaruhi harga mobil ?

# Tujuan proyek
Tujuan dari analisa ini dilakukan adalah untuk mengetahui faktor yang mempengaruhi harga mobil

# langkah solusi yang dilakukan
Untuk mencapai tujuan analisa ini, berikut adalah langkah yang akan dilakukan:
1. Melakukan pembersihan data
2.  Melakukan proses *Exploratory Data Analysis* (EDA) untuk mengetahui faktor-faktor yang  memberikan dampak harga pada mobil
3.   Melakukan analisa korelasi dan regresi
4.   Membuat model dengan Random Forest, KNN dan Boosting
5.   Mengevaluasi model

# Dataset
Data set diambil dari kaggle: https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge

Dataset yang digunakan menunjukkan terdapat 17 kolom atau faktor dalam data set:
1. ID menunjukkan kode mobil
2. Price menunjukkan harga mobil
3. Levy menunjukkan pajak kendaraan
4. Manufacturer menunjukkan perusahaan pembuat
5. Model menunjukkan model mobil
6. Prod. Year menunjukkan tahun pembuatan
7. Category menunjukkan kelompok jenis mobil
8. Fuel type menunjukkan jenis bahan bakar yang digunakan
9. Engine volume menunjukkan ukuran volume mesin
10. Mileage menunjukkan jarak tempuh
11. Cylinders menunjukkan jumlah silinder mesin
12. Gear box menunjukkan transmisi mobil
13. drive wheels menunjukkan posisi setir
14. Doors menunjukkan jumlah pintu
15. Wheel menunjukkan jumlah roda
16. Color menunjukkan warna kendaraan
17. Airbags menunjukkan jumlah airbag dalam kendaraan

Dari 17 data maka akan dicari faktor yang mempengaruhi harga mobil.

# Langkah Project
## 1. Pembersihan data
Tahap pembersihan data dilakukan dengan:
1.1. cek nilai yang hilang,
1.2. cek tipe data yang salah,
1.3. cek normalitas data.

**1.2 Cek nilai yang hilang**
Hasil cek data menunjukkan tidak ada daya kosong karena data konsisten 19237 pada setiap faktor.
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 19237 entries, 0 to 19236
Data columns (total 18 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   ID                19237 non-null  int64  
 1   Price             19237 non-null  int64  
 2   Levy              19237 non-null  object 
 3   Manufacturer      19237 non-null  object 
 4   Model             19237 non-null  object 
 5   Prod. year        19237 non-null  int64  
 6   Category          19237 non-null  object 
 7   Leather interior  19237 non-null  object 
 8   Fuel type         19237 non-null  object 
 9   Engine volume     19237 non-null  object 
 10  Mileage           19237 non-null  object 
 11  Cylinders         19237 non-null  float64
 12  Gear box type     19237 non-null  object 
 13  Drive wheels      19237 non-null  object 
 14  Doors             19237 non-null  object 
 15  Wheel             19237 non-null  object 
 16  Color             19237 non-null  object 
 17  Airbags           19237 non-null  int64  
dtypes: float64(1), int64(4), object(13)
memory usage: 2.6+ MB

Namun demikian ada data - untuk Levya yang menunjukkan bahwa nilai tidak ada. maka pada bagian ini nilai tersebut akan dirubah menjadi nilai 0.

**1.2. Cek tipe data yang salah**
Dari info data menunjukkan adanya tipe data yang tidak sesuai. oleh akrena itu dilakukan penyesuaina data pada faktor: Mileage, Doors, Levy, Cylinders yang semua adalah data object kemudian menjadi data int atau number. Hasilnya adalah sebagai berikut:

car.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 19237 entries, 0 to 19236
Data columns (total 18 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   ID                19237 non-null  int64 
 1   Price             19237 non-null  int64 
 2   Levy              19237 non-null  int64 
 3   Manufacturer      19237 non-null  object
 4   Model             19237 non-null  object
 5   Prod. year        19237 non-null  int64 
 6   Category          19237 non-null  object
 7   Leather interior  19237 non-null  object
 8   Fuel type         19237 non-null  object
 9   Engine volume     19237 non-null  object
 10  Mileage           19237 non-null  int64 
 11  Cylinders         19237 non-null  int64 
 12  Gear box type     19237 non-null  object
 13  Drive wheels      19237 non-null  object
 14  Doors             19237 non-null  int64 
 15  Wheel             19237 non-null  object
 16  Color             19237 non-null  object
 17  Airbags           19237 non-null  int64 
dtypes: int64(8), object(10)
memory usage: 2.6+ MB

**1.3. Melakukan normalisasi data**
Berikut adalah data ekstrem dari variabel harga, tahun, mileage, dan levy.

![image](https://github.com/user-attachments/assets/972321c8-66bf-48f2-9c5c-b4a389b9ba7b)

![image](https://github.com/user-attachments/assets/ea0acbf9-514d-44cf-aff9-f3a8723c69ba)

![image](https://github.com/user-attachments/assets/952e7ccc-a374-4b46-bbdd-516202a98ac1)

![image](https://github.com/user-attachments/assets/9a68f791-8a7c-4362-acef-6a738fcfd324)

Visualisai tersebut menunjukkan data numerik yang tidak normal. Maka dilakukan normalisasi dpada data numerik dengan dengan pendekatan IQR = Q3-Q1. 
Setelah dilakukan normalisasi maka data turun menjadi 10.515 data. dengan contoh hasil adapah sebagai berikut.

![image](https://github.com/user-attachments/assets/5e3aa326-25bd-4657-9d8d-fc8c5888227d)



# 2. Melakukan analisa EDA
Tahap ini dilakukan dengan pendekatan Univariat dan Multivariat

**2.1. Univariat**
Pada analisa ini, data akan dilihat berdasarkan jumlah penjualannya berdasar variabel yang bersifat kategori, sebagai berikut

Jumlah penjualan berdasarkan merk pembuatan

![image](https://github.com/user-attachments/assets/b357bc16-05ce-4873-9389-3a7e0e4dfeaa)

JUmlah penjualan berdasarkan cetegory mobibl

![image](https://github.com/user-attachments/assets/0098e9ea-47e1-4671-8ddf-62fb4f92a59d)

Jumlah penjualan berdasarkan mode transmisi

![image](https://github.com/user-attachments/assets/89188376-61a1-432e-906b-dd4255f036b6)

Jumlah penjualan berdasarkan mode pengerak

![image](https://github.com/user-attachments/assets/2f757afd-a316-40d1-b07c-7709608923fb)


Dari analisa univariat dalam visualisasi tersebut dapat dipahami bahwa merk Hyundai adalah merik yang banyak dibeli yang sekaligus menunjukkan diminati konsumen. Selanjutnya mobil sedan dengan transmisi otomatis dan penggerak roda depan lebih banyak dibeli oleh konsumen.

Cek data untuk variabel numerik
![image](https://github.com/user-attachments/assets/b9903431-38c4-49bc-a3bb-7e455f318d2e)
Dari cek data numerik tersebut dapat diketahui bahwa data untuk harga, mileage, year cenderung normal. Data ini akan diuji lagi nanti.

**2.2. Multivariat**


![image](https://github.com/user-attachments/assets/c41d78ec-4894-4385-bbf0-0e1f45af89e4)








