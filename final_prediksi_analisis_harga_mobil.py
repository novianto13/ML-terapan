# -*- coding: utf-8 -*-
"""Final Prediksi analisis Harga mobil.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V4YYjyVkGVrGtKViqfZsZhqVs1_8AZP7

# Proyek ML Terapan 1: Predictive Analysis - Car Price
# Nama: Novianto
## Data adalah terkait dengan prediksi mobil bekas

Dari data yang akan dianalisa, pertanyaan bisnis yang diajukan adalah:
1. Tipe dan model mobil apa yang paling banyak diminati ?
2. Tipe dan model mobil apa yang memiliki harga tinggi ?
3. Faktor apa yang mempengaruhi harga mobil ?

# Deskripsi Data Penjualan Mobil
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

# load the dataset
url = 'https://raw.githubusercontent.com/novianto13/ML-terapan/main/car_price_prediction.csv' # Changed URL to raw content URL
car_price_prediction = pd.read_csv(url)
car_price_prediction # Display the dataframe, assuming 'car' was intended to be 'car_price_prediction'

# mengganti nama data set
car = car_price_prediction

# Deskripsi dataset

car.info()

"""## Deskrisi dataset

Data menunjukkan bawah terdapat 17 kolom atau faktor dalam data set:
1. ID menunjukkan kode mobil
2. Price menunjukkan harga mobil
3. Levy menunjukkan pajak kendaraan
4. Manufacturer menunjukkan perusahaan pembuat
5. Model menunjukkan model mobil
6. Prod. Year menunjukkan tahun pembuatan
7. Category menunjukkan kelompok jenis mobil
8. Fuel type menunjukkan jenis bahan bakar yang digunakan
9. Engine volume meunjukkan ukuran volume mesin
10. Mileage menunjukkan jarak tempuh
11. Cylinders menunjukkan jumlah silinder mesin
12. Gear box menunjukkan transmisi mobil
13. drive wheels menunjukkan posisi setir
14. Doors menunjukkan jumlah pintu
15. Wheel menunjukkan jumlah roda
16. Color menunjukkan warna kendaraan
17. Airbags menunjukkan jumlah airbag dalam kendaraan

### Evaluasi dataset

Hasil dari deskripsi data tersebut menunjukkan bahwa terdapat 17 kolom atau 17 data yang di record dalam data set. Dari data set tersebut terdapat satu kolom yang jarak atau mileage dengan tipe data object, yang sebaiknya data ini adalah data angka atau int64.
Total data adalah 19.237.

Dari info tersebut diperoleh informasi bahwa semua kolom terlah berisi 19.237 data. dengan demikian dapat dipahami bahwa tidak ada data yang kosong atau hilang dalam dataset tersebut.

Selain itu, pada data doors, tipe data adalah object yang seharusnya int. Sedangkan data yang muncul adalah date.
"""

# statistik deskripsi keseluruhan data

car.describe(include='all')

"""Untuk melihat secara khusus data faktor harga, maka berikut adalah deskripsi statistik untuk harga"""

# Deskripsi data untuk melihat harga mobil

price_desc = car['Price'].describe()
price_desc['count'] = int(price_desc['count']) # Ubah 'count' ke integer
price_desc.loc[['mean', 'std', 'min', '25%', '50%', '75%', 'max']] = price_desc.loc[['mean', 'std', 'min', '25%', '50%', '75%', 'max']].astype(int) # Ubah statistik lainnya ke integer
print(price_desc)

# Melihat harga mobil yang paling rendah

min_price = car['Price'].min()  # Cari nilai 'Price' terendah
lowest_price_data = car[car['Price'] == min_price]  # Filter data dengan 'Price' terendah
print(lowest_price_data)  # Tampilkan data lengkap

"""Dari deskripsi data tersebut dapat dipahami bahwa:
1. Rata-rata harga mobil adalah 18.555
2. Tahun mobil yang terendah adalah 1939, sedangkan yang terbaru adalah tahun 2020.
3. Dalam deskripsi data ini, terdapat data yang ekstrim pada harga, yaitu ada mobil dengan harga yang sangat jauh di atas rata-rata yaitu 26.307.500 dan terdapat harga mobil yang hanya 1.
4. Mobil dengan harga 1, ada 2 mobil yaitu opel dan chevrolet.

# Deskripsi data: memperbaiki data

## Cek nilai 0 atau kosong
"""

# menunjukkan nilai nol

Price = (car.Price == 0).sum()
Levy = (car.Levy == '-').sum()
Prod_year = (car['Prod. year'] == 0).sum()

print("Nilai 0 di kolom price ada: ", Price)
print("Nilai 0 di kolom levy ada: ", Levy)
print("Nilai 0 di kolom Prod.year ada: ", Prod_year)

"""Informasi di atas menunjukkan bahwa tidak ada nilai 0 dalam harga dan tahun, sedangkan ada nilai - (kosong) pada faktor Lavy. Karena Levy adalah pungutan pajak kendaraan maka niali tersebut menunjukkan bahwa tidak ada pungutan atau pajak untuk kendaraan tersebut. dalam data terdapat 5819 data Levy yang tidak memiliki nilai pungutan.

## Memperbaiki tipe data

Langkah penting selanjutnya adalah memperbaiki tipe data yang tidak sesuai
"""

# memperbaiki nilai mileage menjadi angka
car['Mileage'] = car['Mileage'].str.replace('km', '', regex=False).astype(int)

# memperbaiki nilai doors menjadi angka
car['Doors'] = car['Doors'].str.extract('(\d+)').astype(int)

# Replace hyphens or any non-numeric characters with NaN before converting to int
car['Levy'] = pd.to_numeric(car['Levy'], errors='coerce').fillna(0).astype('int64')

# mengganti tipe silinder menjadi numerik
car['Cylinders'] = car['Cylinders'].astype('int64')

car.info()

"""Tipe data yang diperbaiki adalah mileage, levy, cylinders, dan doors, yang awalnya adalah object diganti dengan int (number).

Hasil secara keseluruhan adalah sebagai berikut
"""

# deskripsi dataset setelah perbaikan

car

"""## Mengganti nama Prod. year menjadi year"""

car = car.rename(columns={'Prod. year': 'year'})

car.info()

"""## Melihat nilai outlier

Langkah ini akan mengevaluasi adanya data outlier
"""

sns.boxplot(x=car['Price'])

sns.boxplot(x=car['year'])

sns.boxplot(x=car['Mileage'])

sns.boxplot(x=car['Levy'])

sns.boxplot(x=car['Doors'])

"""Dari diagram boxplot tersebut tampak data ekstrem ada pada nilai harga. terdapat satu nilai harga yang sangat ekstrem berbeda. oleh karena itu data outlier ini perlu dihapus. Sedangkan data lainnya juga terdapat nilai yang diluar jangkauan atau outlier."""

# Melihat mobil dengan harga tertinggi

max_price = car['Price'].max()  # Cari nilai 'Price' tertinggi
highest_price_data = car[car['Price'] == max_price]  # Filter data dengan 'Price' terendah
print(highest_price_data)  # Tampilkan data lengkap

"""### Menghapus data outlier

Karena rentang data yang begitu besar maka data outlier akan dihapus.
"""

# Mencari nilai maksimum pada kolom 'Price'
max_price = car['Price'].max()

# Menghapus baris dengan nilai 'Price' sama dengan nilai maksimum
car = car[car['Price'] != max_price]

# menormalkan data dengan menghapus data outlier
# Select only numeric columns for quantile calculation
numeric_car = car.select_dtypes(include=np.number)
Q1 = numeric_car.quantile(0.25)
Q3 = numeric_car.quantile(0.75)
IQR = Q3 - Q1

# Filter outliers based on numeric columns
car = car[~((numeric_car < (Q1 - 1.5 * IQR)) | (numeric_car > (Q3 + 1.5 * IQR))).any(axis=1)]

# Cek ukuran dataset setelah kita drop outliers
car.shape

car.info()

"""Setelah data outlier dihapus, maka jumlah data terbaru adalah 10.515 data.

Berikut adalah visualisasi dari data tersebut.
"""

# Cek normalisasi data harga

sns.boxplot(x=car['Price'])

# meiihat dataset dengan urutan harga tertinggi

car_sorted = car.sort_values(by=['Price'], ascending=False)
print(car_sorted)

"""Dari data yang ditampilkan maka dapat dihapus nilai extreme dari harga, sedangkan nilai lainnya tidak dihapus supaya tidak menghilangkan makna nilai data.

## Analisa Univariat

Pada bagian ini, akan dilakukan analisa dataset dengan pendekatan Univariat.
"""

# membuat kategori data
numerical_features = ['Price', 'year', 'Mileage', 'Levy', 'Cylinders', 'Doors', 'Airbags']
categorical_features = ['Manufacturer', 'Category', 'Gear box type', 'Drive wheels']

# menampilkan jumlah data sesuai dengan pembuat kendaraan
feature = categorical_features[0]
count = car[feature].value_counts()
percent = 100*car[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Dari analisa diatas, dapat dipahami bahwa mobil dari pabrikan hyundai, toyota, Chevrolet, Honda, dan Ford merupakan 5 nilai penjualan tertinggi."""

# menampilkan data untuk berdasarkan kategori produk
feature = categorical_features[1]
count = car[feature].value_counts()
percent = 100*car[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Dari grafik diatas, dapat dipahami bahwa mobil dengan tipe sedan merupakan mobil dengan tingkat penjualan tertinggi. disusul jeep dan hatchback"""

# menampilkan produk berdasarkan gear box
feature = categorical_features[2]
count = car[feature].value_counts()
percent = 100*car[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""dari data tersebut dapat dipahami bahwa mobil dengan tipe otomatis merupakan mobil dengan tingkat penjualan tertinggi. sedangkan mobil dengan tipe CVT merupakan mobil dengan tingkat penjualan terendah."""

# menampilkan produk berdasarkan  drives wheels
feature = categorical_features[3]
count = car[feature].value_counts()
percent = 100*car[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Dari grafik tersebut menunjukkan bahwa mobil dengan penggerak roda depan memiliki tingkat penjualan tertinggi."""

# analisa nilai angka pada data numerik
car.hist(bins=50, figsize=(20,15))
plt.show()

"""Dari diagram diatas, dapat diketahui bahwa data untuk harga, mileage, year cenderung normal.

# Analisa Multivariat

Pada bagian ini, data akan dikommperasikan terhadap harga.
"""

cat_features = car.select_dtypes(include='object').columns.to_list()

for col in cat_features:
  sns.catplot(x=col, y="Price", kind="bar", dodge=False, height = 4, aspect = 3,  data=car, palette="Set3")
  plt.title("Rata-rata 'Price' Relatif terhadap - {}".format(col))

"""Untuk menjawab pertanyaan bisnis 1 dan 2, dari data tersebut dapat dipahami bahwa:
1. mobil dengan warna kuning memiliki rata-rata harga lebih tinggi.
2. mobil dengan kendali roda kiri lebih tinggi harganya dari pada roda kanan.
3. harga mobil dengna mode rear lebih tinggi harnyanya dari tipe mobil, front dan 4x4 wheel drive
4. mobil dengan transmisi triponinc lebih mahal dari pada rata rata harga pite kendaraan lain.
5. mobil dengan interior kulit akan memiliki rata-rata harga leih tinggi dari pada yang tidak kulit.
6. mobil tipe universal memiliki rata-rata harga tertinggi.
"""

# Mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(car, diag_kind = 'kde')

"""Dari diagram tersebut dapat dipahami bahwa secara data numerik tidak ada data yang menunjukkan pengaruh jelas terhadap variabel atau faktor harga.

Oleh karena itu untuk melihat kaitan antara satu hariabel dengan variabel lain maka perlu dilihat korelasinya, sebagai berikut:


"""

# evaluasi Korelasi atau hubungan

plt.figure(figsize=(10, 8))
correlation_matrix = car[numerical_features].corr().round(2)

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""Dari analisa heatmap tersebut, dapat dipahami bahwa
1. hanya faktor tahun dan harga yang memiliki hubungan sebesar 0.28. Nilai ini menunjukkan hubungan positif artiknya, semakin baru maka harga bisa semakin tinggi.
2. Variabel harga memiliki hubungan yang negatif terhadap mileage atau jarak. hubungan negatif ini menunjukkan jarak tempuh mobil akan menurunkan harga jualnya.
3. Heatmap juga menunjukkan bahwa ada hubungan antara levy dengan years sebesar 0.4. Hal ini berarti bahwa semakin baru tahun maka pajak akan semakin tinggi, namun nilai tersebut masih rendah karena masih dibawah 0.5

# Encoding Fitur Kategori
"""

from sklearn.preprocessing import  OneHotEncoder
car = pd.concat([car, pd.get_dummies(car['Manufacturer'], prefix='Manufacturer')],axis=1)
car = pd.concat([car, pd.get_dummies(car['Category'], prefix='Category')],axis=1)
car = pd.concat([car, pd.get_dummies(car['Gear box type'], prefix='Gear box type')],axis=1)
car = pd.concat([car, pd.get_dummies(car['Drive wheels'], prefix='Drive wheels')],axis=1)
car = pd.concat([car, pd.get_dummies(car['Model'], prefix='Model')],axis=1)
car = pd.concat([car, pd.get_dummies(car['Color'], prefix='Color')],axis=1)
car = pd.concat([car, pd.get_dummies(car['Leather interior'], prefix='Leather interior')],axis=1)
car = pd.concat([car, pd.get_dummies(car['Fuel type'], prefix='Fuel type')],axis=1)
car.drop(['Manufacturer','Category','Gear box type', 'Drive wheels', 'Model', 'Color','Leather interior', 'Fuel type', 'Wheel', 'Engine volume'], axis=1, inplace=True)
car.head()

# Mengubah nilai boolean menjadi integer (0 dan 1)
for column in car.select_dtypes(include=['bool']).columns:
    car[column] = car[column].astype(int)

car.head()

"""# Uji Regresi

/dari hasil analisa pairplot dan heatmap yang dilakukan maka dapat diperoleh informasi bahwa hanya faktor tahun yang memiliki nilai korelasi lebih dari 0.2, yaitu 0.28. Dengan demikian hanya variabel tahun saja yang dapat menjelaskan harga dengan lebih baik dari pada variabel lain.

Oleh karena itu, prediksi akan dilakukan hanya pada variabel tahun terhadap harga.

Berikut ini adalah gambaran regresinya untuk melihat arah regresinya.

"""

# Buat figure dan axes
fig, ax = plt.subplots(figsize=(8, 6))

# Scatterplot
sns.scatterplot(x='year', y='Price', data=car, ax=ax, label='Data')

# Regplot
sns.regplot(x='year', y='Price', data=car, ax=ax, scatter=False, label='Regression Line')  # scatter=False untuk menghindari plot titik dua kali

# Atur judul, label sumbu, dan legenda
plt.title('Scatterplot dan Regplot Harga vs Tahun')
plt.xlabel('Tahun')
plt.ylabel('Harga')
plt.legend()

# Tampilkan plot
plt.show()

"""Hasil plot tersebut menunjukkan menunjukkan arah positif yang menunjukkan semkin baru tahun maka harga akn cenderung lebih mahal.
Untuk mendukung hal itu maka regresi dapat dilakukan sebagai berikut
"""

import statsmodels.formula.api as smf
model = smf.ols('Price ~ year', data=car).fit()
print(model.summary())

"""Hasil regresi tersebut menunjukkan bahwa nilai P sebesar 0.000 yang artinya terbukti bahwa semakin baru tahun mobil maka harga semakin tinggi, dengan nilai koefisien 827.54. yang menunjukkan kenaikan harga sebesar 827.54 untuk tahun kendaraan yang lebih baru.

# Standarisasi

Selanjutnya kita akan melihat seberapa tepat akurasi prediksi tahun terhadap harga dengan melakukan standarisasi nilai.
"""

from sklearn.model_selection import train_test_split

    X = car.drop(["Price"],axis =1)
    y = car["Price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)

from sklearn.preprocessing import StandardScaler

    numerical_features = ['year']
    scaler = StandardScaler()
    scaler.fit(X_train[numerical_features])
    X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
    X_train[numerical_features].head()

X_train[numerical_features].describe().round(4)

"""# Pembuatan Model

## KNN
"""

# Siapkan dataframe untuk analisis model
    models = pd.DataFrame(index=['train_mse', 'test_mse'],
                          columns=['KNN', 'RandomForest', 'Boosting'])

from sklearn.neighbors import KNeighborsRegressor
    from sklearn.metrics import mean_squared_error

    knn = KNeighborsRegressor(n_neighbors=10)
    knn.fit(X_train, y_train)

    models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""## Random Forest"""

# Impor library yang dibutuhkan
    from sklearn.ensemble import RandomForestRegressor

    # buat model prediksi
    RF = RandomForestRegressor(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
    RF.fit(X_train, y_train)

    models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""## Boosting Algorithm"""

from sklearn.ensemble import AdaBoostRegressor

    boosting = AdaBoostRegressor(learning_rate=0.05, random_state=55)
    boosting.fit(X_train, y_train)
    models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""# Evaluasi Model"""

# Lakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan varians=1
    X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

# Buat variabel mse yang isinya adalah dataframe nilai mse data train dan test pada masing-masing algoritma
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])

# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}

# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3

# Panggil mse
mse

fig, ax = plt.subplots()
    mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
    ax.grid(zorder=0)

prediksi = X_test.iloc[:1].copy()
    pred_dict = {'y_true':y_test[:1]}
    for name, model in model_dict.items():
        pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

    pd.DataFrame(pred_dict)

"""### Kesimpulan

Dari hasil tersebut uji model tersebut, model menggunakan Random Forest menunjukkan eror yang lebih sedikit dari pada nilai KNN dan Boosting.

Hasil ini menunjukkan nilai prediksi RF 32381.8 yang berarti 79.43% akurasi prediksi tersebut.

Pada bagian akhir ini, jawaban atas pertanyaan bisnis adalah sebagaiberikut:
1. Faktor yang mempredikisi harga mobil adalah faktor tahun yang ditunjukkan dengan korelasi atau hubungan yang paling kuat diantara faktor lain.
Dengan demikiansemakin baru tahun kendaraan maka harga akan mengalami peningkatan.
2. Faktor harga dapat memprediksi sebesar 79.54% peningkatan harga mobil.
"""