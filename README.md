# Laporan Proyek Machine Learning - Novianto
## Domain Proyek
Masalah yang Dihadapi
Dalam industri otomotif, menentukan harga jual kendaraan merupakan tantangan yang kompleks. Harga mobil dipengaruhi oleh berbagai faktor, seperti merek, model, tahun pembuatan, spesifikasi teknis, kondisi kendaraan, serta tren pasar, yang menimbulkan ketidakpastian.

Latar Belakang pemilihan masalah adalah pertumbuhan pasar otomotif. Industri otomotif global terus berkembang, dengan meningkatnya minat pada pasar mobil baru dan bekas. Untuk bersaing, perusahaan perlu memahami faktor-faktor yang memengaruhi harga kendaraan dengan lebih baik.

## Business Understanding
Berbagai macam mobil yang ada dengan berbagai kondisi membuat sulit untuk memperkirakan harga yang mobil. Oleh karena itu, analisa diperlukan untuk memberikan prediksi harga mobil dengan kondisi yang beragam. Oleh karena itu, masalah yang coba diselesaikan dari kondisi pasar mobil ini adalah:
1. Tipe mobil apa yang paling diminati.
2. Tipe modil apa yang memiliki harga tinggi.
3. faktor apa yang mempengaruhi harga mobil.

### Problem Statements
Dari masalah bisnis yang ada tersebut maka pernyataan masalah bisnis yang diajukan adalah:
1. Apakah tipe dan model mobil yang paling banyak diminati ?
2. Apakah tipe dan model mobil yang memiliki harga tinggi ?
3. Apakah faktor yang mempengaruhi harga mobil ?

### Goals
Berdasarkan problem statements yang diajukan, tujuan proyek ini dirancang untuk menyelesaikan masalah bisnis dan memberikan wawasan strategis. Berikut adalah goals proyek yang menghubungkan masalah dengan solusi:

1. Mengidentifikasi Tipe dan Model Mobil yang Paling Banyak Diminati
Masalah: Tidak ada data pasti mengenai jenis dan model mobil yang paling diminati oleh pasar.
Tujuan: Menghasilkan wawasan tentang tren preferensi konsumen berdasarkan data penjualan, fitur kendaraan, atau ulasan. Hal ini akan membantu dealer dan produsen menyusun strategi pemasaran yang lebih efektif.

2. Menganalisis Tipe dan Model Mobil dengan Harga Tinggi
Masalah: Tidak ada pemahaman yang jelas tentang tipe dan model mobil yang cenderung memiliki harga tinggi di pasar.
Tujuan: Mengidentifikasi kategori kendaraan (merek, model, atau fitur premium) yang berkontribusi terhadap segmen harga tinggi. Informasi ini dapat digunakan oleh produsen untuk menargetkan segmen premium secara strategis.

3. Mengidentifikasi Faktor-Faktor yang Mempengaruhi Harga Mobil
Masalah: Penentuan harga mobil yang optimal sering kali kompleks karena melibatkan berbagai variabel.
Tujuan: Mengembangkan model yang mampu memprediksi harga mobil berdasarkan faktor-faktor seperti spesifikasi teknis, tahun produksi, kondisi kendaraan, dan lainnya. Hal ini bertujuan untuk memberikan panduan harga yang lebih akurat bagi dealer dan konsumen.

Kreteria:
Untuk jawaban nomer 3, diperlukan suatu ukuran untuk dapat menilai faktor atau variabel yang mempengaruhi harga: yaitu korelasi di atas 0.2 dan regresi dengan nilai P lebih rendah dari Tingkat kesalahan 5%. Sedangkan prediksi model adalah di atas 70%

### Solution Statement
Untuk mencapai tujuan analisa ini, berikut adalah langkah yang akan dilakukan:
1. Melakukan pembersihan data
2.  Melakukan proses *Exploratory Data Analysis* (EDA) untuk mengetahui faktor-faktor yang  memberikan dampak harga pada mobil
3.   Melakukan analisa korelasi dan regresi
4.   Membuat model dengan Random Forest, KNN dan Boosting
5.   Mengevaluasi model

## Data Understanding
Dataset Ccar_prediction diambil dari kaggle: https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge

Dataset dirubah dengan nama car untuk mempermudah analisa. Dataset car yang digunakan menunjukkan terdapat 17 kolom atau faktor dalam data set dan terdapat 19.237 baris atau data dalam dataset, yaitu :

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

**Info data pada dataset adalah sebagai berikut:**

Dataset 'car' memiliki 19237 baris dan 17 kolom. Ini berarti ada 19237 observasi (mobil) dan 17 atribut atau fitur yang mendeskripsikan setiap mobil.

Terdapat beberapa tipe data dalam dataset:

int64: 'ID', 'year', 'Cylinders', 'Doors', 'Airbags'
float64: 'Price', 'Levy', 'Engine volume'
object: 'Manufacturer', 'Model', 'Category', 'Leather interior', 'Fuel type', 'Gear box type', 'Drive wheels', 'Color', 'Wheel', 'Mileage' Tipe data object biasanya menunjukkan data tekstual atau kategorikal.

Kolom 'Mileage' awalnya memiliki tipe data 'object' tetapi kemudian diubah menjadi 'int64' dalam kode Anda. Hal ini menunjukkan bahwa kolom tersebut awalnya berisi data non-numerik (kemungkinan termasuk satuan "km") yang kemudian dibersihkan dan dikonversi menjadi angka yang mewakili jarak tempuh dalam kilometer.

Kolom 'Levy' awalnya memiliki tipe data 'object' tetapi kemudian diubah menjadi 'int64' dalam kode Anda. Hal ini menunjukkan bahwa kolom tersebut awalnya berisi data non-numerik (kemungkinan termasuk simbol '-') yang kemudian dibersihkan dan dikonversi menjadi angka yang mewakili pajak kendaraan.

Kolom 'Doors' awalnya memiliki tipe data 'object' tetapi kemudian diubah menjadi 'int64' dalam kode Anda. Hal ini menunjukkan bahwa kolom tersebut awalnya berisi data non-numerik (kemungkinan termasuk teks "doors") yang kemudian dibersihkan dan dikonversi menjadi angka yang mewakili jumlah pintu.

Kolom 'Cylinders' awalnya memiliki tipe data 'float64' tetapi kemudian diubah menjadi 'int64' dalam kode Anda. Hal ini menunjukkan bahwa kolom tersebut awalnya berisi data angka desimal yang kemudian dikonversi menjadi angka bulat yang mewakili jumlah silinder mesin.

Semua kolom memiliki 19237 nilai non-null. Ini menunjukkan bahwa tidak ada nilai yang hilang (missing values) dalam dataset. Namun, perlu diingat bahwa beberapa nilai mungkin awalnya kosong atau tidak valid dan telah diubah atau diisi selama proses pembersihan data (misalnya, nilai '-' pada kolom 'Levy').

Dataset menggunakan memori sebesar 3.5+ MB. Ini merupakan indikasi ukuran dataset dan kompleksitasnya.


### 1. Cek nilai data:
Tahapan evaluasi nilai data dilakukan dengan tahapan sebagai berikut:
A. cek nilai yang hilang,
B. cek tipe data yang salah,
C. cek normalitas data.

**A. Cek nilai yang hilang**
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

**B. Cek tipe data yang salah**
Dari info data menunjukkan adanya tipe data yang tidak sesuai yaitu: Mileage, Doors, Levy, Cylinders yang semua adalah data object kemudian menjadi data int atau number. Hasilnya adalah sebagai berikut:

1. Kolom Mileage: tipe data object, yang menunjukkan adanya karakter non-numerik (seperti "km"). Data ini dapat diubah menjadi int64 Ini adalah langkah yang tepat.
2. Kolom Doors: tipe data object, padahal seharusnya berupa angka yang mewakili jumlah pintu. Data ini dapat diubah menjadi int64 Ini adalah langkah yang tepat, dengan mengekstrak angka menggunakan str.extract dan mengubahnya menjadi int64. Ini juga langkah yang tepat.
3. Kolom Levy: Awalnya bertipe data object, yang menunjukkan adanya karakter non-numerik (seperti "-").
4. Kolom Cylinders: tipe data float64, yang mungkin kurang sesuai karena jumlah silinder biasanya berupa bilangan bulat. 

Kolom Engine volume: Bertipe data float64, yang mungkin perlu dikaji lebih lanjut. Jika volume mesin selalu dinyatakan dalam bilangan bulat, Anda dapat mempertimbangkan untuk mengubahnya menjadi int64. Namun, jika ada nilai desimal yang valid, maka tipe data float64 sudah tepat.

car.info()

![image](https://github.com/user-attachments/assets/cf18baa4-4a67-4bc3-a2f7-77d1b3aefba9)


**C. Cek normalisasi data**
Berikut adalah data ekstrem dari variabel harga, tahun, mileage, dan levy.

![image](https://github.com/user-attachments/assets/972321c8-66bf-48f2-9c5c-b4a389b9ba7b)

![image](https://github.com/user-attachments/assets/ea0acbf9-514d-44cf-aff9-f3a8723c69ba)

![image](https://github.com/user-attachments/assets/952e7ccc-a374-4b46-bbdd-516202a98ac1)

![image](https://github.com/user-attachments/assets/9a68f791-8a7c-4362-acef-6a738fcfd324)

Visualisai tersebut menunjukkan data numerik yang tidak normal. Maka dilakukan normalisasi dpada data numerik dengan dengan pendekatan IQR = Q3-Q1. 
Setelah dilakukan normalisasi maka data turun menjadi 10.515 data. dengan contoh hasil adapah sebagai berikut.

![image](https://github.com/user-attachments/assets/5e3aa326-25bd-4657-9d8d-fc8c5888227d)


### 2. Melakukan analisa EDA
Tahap ini dilakukan dengan pendekatan Univariat dan Multivariat

** Analisa Univariat**
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

** Analisa Multivariat**
PAda analisa mulivariat, kita akan menggambungkan dua variabel atau faktor untuk mendapatkan informasi yang lebih luas. Sesuai dengan tujuan dari analisa ini, maka variabel atau faktor harga akan dikaitkan dengan variabel kategori, antara lain: category,interrior, fuel type, gear box, drive wheel.

![image](https://github.com/user-attachments/assets/ee61856b-601b-402f-a1c2-58dccbe3a5b4)

![image](https://github.com/user-attachments/assets/c41d78ec-4894-4385-bbf0-0e1f45af89e4)

![image](https://github.com/user-attachments/assets/5099f57e-a6c8-4b63-b343-493be1970b88)

![image](https://github.com/user-attachments/assets/3f2a706f-c4f8-4dc4-ad42-72c41b4da34f)

![image](https://github.com/user-attachments/assets/dc517d13-b106-4eac-b6b3-f6ced9b7c3ab)

![image](https://github.com/user-attachments/assets/b4f04ea8-dd6c-4fc8-a700-41a883a251e0)


Hasil visualisasi multivariat di atas menunjukkan:
1. Mobil dengan category universal memiliki harga lebih tinggi dari pada jenis mobil lainnya.
2. Desain interior yang berbahan kulit memiliki harga yang lebih mahal.
3. Mobil dengan mesin diesel memiliki hargal yang relatif lebih mahal dari jenis mesin yang lain.
4. Mobil dengan transmisi tiptronic memilik harga yang lebih mahal
5. Mobbil dengan roda penggerak belakang memiliki harga yang lebih mahal dari yang jenis lainnya
6. Mobil dengan warna kuning memiliki harga yang relatif lebih mahal dari warna lainnya

Setelah kita mengetahui kaitan harga denga beberapa variabel kategori, maka selanjutnya kita akan melihat kaitan harga dengan variabel numerik lain. hasilnya adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/1c02d766-a684-4cb7-bad2-feed771f1eda)

Dari hasil visualisasi tersebut, tampak bahwa tidak ada data numerik yang memiliki pengaruh langsung dengan harga. Untuk mengevaluasinya, maka kita dapat melihat dalam matrix heatmap berikut ini:

![image](https://github.com/user-attachments/assets/a6906571-1d28-4f79-9c13-420c48641671)

Dari matrik heatmap tersebut, tampak hanya variabel tahun yang memiliki nilai hubungan tertinggi dibandingkan dengan variabel numerik lainnya yaitu 0.28. Dengan demikian hanya tahun yang memiliki kaitan dengan harga.


## Data Preparation
Teknik data preparation akan dilakukan dengan tahapan sebagai berikut:

### Feature Engineering
Tahap ini dilakukan untuk mempersiapkan data dapat diolah lebih lanjut

**1. Perbaikan tipe data**
Hasil dari data understandeing menunjukkna bahwa tidak ada yang hilang pada dataset ini. Sehingga perbaikan dilakukan untuk memperbaiki data.

1. Kolom Mileage: tipe data object, yang menunjukkan adanya karakter non-numerik (seperti "km"). Data ini dapat diubah menjadi int64 Ini adalah langkah yang tepat.
2. Kolom Doors: tipe data object, padahal seharusnya berupa angka yang mewakili jumlah pintu. Data ini dapat diubah menjadi int64 Ini adalah langkah yang tepat, dengan mengekstrak angka menggunakan str.extract dan mengubahnya menjadi int64. Ini juga langkah yang tepat.
3. Kolom Levy: Awalnya bertipe data object, yang menunjukkan adanya karakter non-numerik (seperti "-").
4. Kolom Cylinders: tipe data float64, yang mungkin kurang sesuai karena jumlah silinder biasanya berupa bilangan bulat.

Hasilnya adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/c754c557-61b6-497d-b50b-029f0e8667d2)

**2. Normalisasi data**
Hasil data understantding menunjukkan adanya data ekstreme. oleh karena itu normalisasi dilakukan, khususnya pada variabel harga. Hasilnya adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/2573a27b-80f7-4965-843b-397c467f2b74)

Setelah dilakukan normalisasi data, maka dataset menjadi 10515 data

![image](https://github.com/user-attachments/assets/34549d87-a080-4a3c-b858-c2e318f778d9)


### Standarisasi



## Modeling: Korelasi dan regresi
Hasil matrik heatmap menunjukkan nilai korelasi harga dengan tahun yang lebih baik dari pada variabel lainnya. Namun demikian kita perlu mengevaluasi dengan labih baik dengan melakukan uji regresi. Uji regresi dilakukan dengan dengan kriteria nilai P lebih rendah dari 0.05 (5%)

Uji regresi dilakukan dengan pendekatan linear regression OLS dari library statmodel. Hasilnya adalah sebagai berikut:
                          
                Year                              
1. coef =       827.5463
2. std err =      28.153
3.   t =          29.394
4. P>|t| =         0.000 
5. 0.025 =       772.360
6. 0.975 =       882.732

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.05e+06. This might indicate that there are
strong multicollinearity or other numerical problems.

Dari hasil tersebut, maka dapat diketahui bahwa tahun memiliki pengaruh terhadap harga dengan melihat nilai P sebesar 0.000. Dengan nilai koefisien sebesar 827.54, hasil regresi memasikan bahwa tahun memiliki pengaruh pada harga. Nilai koefisien yang positif ini menunjukkan bahwa terdapat hubungan positf, yaitu semakin baru tahyn kedaraan maka semakin tinggi harganya, dengan kenaikan sebesar 827.54. 

Untuk memastikan nilai tersebut maka dilakukan uji model.

## Evaluasi model dan evaluasi model
Pembuatan model dilakukan dengan melakukan standarisasi supaya nilai lebih normal. Kemudian Model yang dibuat adalah dengan Random Forest, KNN danBoosting Algorithm

Hasil uji model adalah tersebagai berikut:

                 train	       test
1. KNN =     	68211.830462 	81260.940738
2. RF =       	8727.114406 	23225.015087
3. Boosting =	73626.970477 	76027.696185

![image](https://github.com/user-attachments/assets/aa5583c3-a1c2-46b5-8d35-b653fe68a988)

Dari visualisasi tersebut dapat diperoleh pemahaman bahwa model dengan menggunakan Random forest menghasilkan eror yang lebih sedikit, dan hasil test yang lebih tinggi, sehingga model RF lebih baik dari pada yang model yang lainnya.

1. y_true =	              40769
2. prediksi_KNN =	      27158.4 (66%)
3. prediksi_RF =	       32381.8 (79%)
4. prediksi_Boosting =  17779.6 (43%)

## Kesimpulan
Analisa ini dilakukan untuk mengetahui faktor atau variabel yang dapat memperngaruhi harga mobil. Oleh karena itu, hasil penelitian ini menjawab tertanyaan bisnis:

1. Tipe dan model mobil apa yang paling banyak diminati ?
Mobil yang paling banyak diminati adalah mobil jenis sedan dengan transmisi otomatis dan roda penggerak depan. Banyaknya permintaan terhadap jenis produk ini dapat disebabkan oleh harga produk sedan masuk kategori kendaraan yang harganya tidak mahal selain hatchbank, goods wagon, dan cabriolet. Selain itu, harga transmisi otomatis dan roda penggrak depan tidak semahal transmisi tiptronic dan harganya telatif hampir sma dengan transmisi Variator. Termasuk juga roda penggerak depan lebih murah dari pada penggerak balakang.

Dengan demikian, produksi sedan dengan transmisi otomatis akan lebih diminati.


3. Tipe dan model mobil apa yang memiliki harga tinggi ?
Dari hasil analisa, harga mobil akan lebih tinggi jika mememiliki unsur interior kulit, dengan transmisi tiptronic dan berbahan bakar diesel dengan model mobil adalah kendaraan universal. Mobil yang masuk kategori-kategori tersebut akan cenderung memiliki harga lebih mahal.

5. Faktor apa yang mempengaruhi harga mobil ?
Dari uji korelasi dan regresi, maka variabel tahun adalah yang a=paling menunjukkan kaitan dengan harga. Dengan demikian tahun kendaraan yang relaitf baru akan memiliki ralatif harga yang lebih mahal sebesar 827.54.

Nilai koefisien ini dapat diprediksi dengan oleh model dengan Random forest. 





