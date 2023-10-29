# Laporan Proyek Machine Learning
### Nama  : Rohmat
### NIM   : 211351131
### Kelas : TIF Pagi B



## Domain Proyek
Dapat dilihat bahwa Smartphone telah menjadi bagian integral dari kehidupan sehari-hari banyaknya individu, Selain menjadi alat komunikasi, tetapi juga sebagai alat produktivitas,Hiburan,Pengelolaan Keuangan, dan berbagai aktivitas lainnya. Namun masih banyak juga orang yang belum mengetahui pasti harga dari smartphone sesuai spesifikasi yang di inginkan jadi jika ingin mengetahuinya harus pergi ke tempat penjual smartphone tersebut untuk menanyakan harga sesuai spesifikasi yang di inginkan, Oleh karena itu saya membuat sebuat proyek yang akan mengestimasi harga dari smartphone tersebut mulai dari  Jenis Brand, jenis processor,RAM,ROM dan lainnya.

## Business Understanding
Proyek ini memudahkan, menghemat waktu dan tenaga kita, karena dapat mengestimasi harga dari smartphone yang sesuai dengan spesifikasi yang kita inginkan, kita dapat memperkirakan harga dari sebuah smartphone tanpa harus pergi dan bertanya ke penjualnya terlebih dahulu

### Problem Statments
- Pembeli atau konsumen tidak dapat memperkirakan harga sesuai dengan sfesifikasi yang di inginkan

### Goals
- Memprediksi harga smartphone sesuai dengan spesifikasi yang di inginkan
  
### Solution statements
- Membuat sebuah Platform estimasi harga smartphone berbasis web agar memudahkan orang orang memprediksi harga smartphone sesuai spesifikasi yang di inginkan

## Data Understanding
Dataset yang diganakan adalah dataset Mobile Price 2023 yang di ambil dari kaggle, yang berisi sekumpulan data smartphone  di tahun 2023

[Mobile Price Data 2023](https://www.kaggle.com/datasets/krishnendujana2/mobile-price).

### Variable-variable pada Dataset Mobile Price Data 2023 adalah sebagai berikut :
 - Name : Merupakan Nama Dari Jenis atau type smartphone (Type data : Object) 
 - Brand_Name : Merupakan Merek Smartphone (Type data : Object)
 - Processor : Merupakan nama dari Processor smartphone yang digunakan (Type data : Object) 
 - BrandCategory : Merupakan id dari jenis Brand yang digunakan oleh smartphone (Type data : int) 
 - ProcessorCategory :  Merupakan id dari jenis processor yang digunakan oleh smartphone (Type data : int) 
 - Rating : Merupakan penilaian yang diberikan kepada smartphone oleh pengguna (Type data : float)
 - Numbe_of_Ratings : Merupakan Jumlah penilaian/rating yang di berikan pengguna (Type data : float)
 - Number_of_Reviews : Merupakan Jumlah Total ulasan/review yang di tulis oleh pengguna (Type data : float)
 - RAM : Merupakan kapasitas RAM yang dimiliki oleh smartphone tersebut (Type data : int)  
 - ROM : Merupakan Kapasitas  penyimpanan internal yang dimiliki oleh smartphone tersebut (Type data : int)  
 - Diplay_Size : Merupakan ukuran layar smartphone (Type data : float)
 - Back_Camera : Merupakan Spesifikasi kamera belakang dari smartphone (Type data : float)
 - Front_Camera : Merupakan Spesifikasi kamera depan dari Smartphone (Type data : float)
 - Battery : Merupakan Kapasitas Baterai Smartphone (Type data int)  
 - Price : Merupakan Harga Dari Smartphone dalam mata uang tertentu (Type data : int)  
 - Price_Range : Merupakan Kategori atau rentang harga Smartphone (Type data :int)

## Data Preperation

### Menghubungkan dengan Kaggle lalu input Datasets dari kaggle

Pertama kita harus terhubung dulu dengan kaggle, dengan cara mendownload Token dari kaggle terlebih dahulu, setelah mendapatkan token kita bisa langsung memasukan peritah di bawah ini dan masukan token yang sudah di download.
```bash
from google.colab import files
files.upload()
```
Langkah selanjutnya adalah membuat direktori
```bash
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle
```
Setelah direktori di buat kita bisa langsung memanggil url dataset dari kaggle tersebut dengan cara mengcopy API command nya
```bash
! kaggle datasets download -d krishnendujana2/mobile-price
```
Setelah dataset nya berhasil terpanggil kita harus meng ekstrak dataset tersebut dengan cara memasukan perintah seperti berikut ini :
```bash
! mkdir mobile-price
! unzip mobile-price.zip -d mobile-price
! ls mobile-phone-specifications-and-prices
```
Setelah berhasil terhubung dengan kaggle dan dataset kita sudah bisa mulai untuk melakukan reading data

### Membaca data
Pertama kita bisa mengimport liblary yang akan kita gunakan terlebih dahulu
```bash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```
Lalu kita bisa memanggil dataset yang sudah kita download dan ekstrak di atas agar bisa kita baca datanya, adalah sebagai berikut :
```bash
df = pd.read_csv('/content/mobile-price/mobilepricedata.csv')
```
Setelah kita panggil kita dapat melakukan beberapa exploratory data analysis sederhana, Kita bisa mulai dari menampilkan dataset dan melihat jumlah kolom nya, lalu mengecek type data dan lainnya
```bash
df.head()
```
```bash
df.info()
```
```bash
df.describe
```
Kita juga bisa mencoba untuk menghapus kolom 'Name', 'Brand_Name', 'Processor', dan 'Price_Range' dari dataset, dan menyimpan fitur-fitur yang tersisa dalam variabel x. dan membuat Kolom 'Price_Range' sebagai target. Itu dilakukan agar kita dapat memisahkan variabel-variabel yang akan digunakan sebagai fitur atau faktor-faktor dalam analisis atau pemodelan dari variabel yang ingin kita prediksi.
```bash
x =df.drop(['Name','Brand_Name','Processor','Price_Range'],axis = 1)
y = df.Price_Range
x.head(5)
```
```bash
x.info()
```
Kita juga bisa mengecek apakah terdapat duplicate data di dalam dataset kita
```bash
df[df.duplicated()]
```
Setelah kita melakukan reading data kita bisa melanjutkan ke langkah selanjutnya yaitu visualisasi data

### Visualisasi Data

Pertama kita bisa cek heatmap dari datasets yang kita gunakan, apakah terdapat data yang kosong atau tidak, kita bisa gunakan perintah ini untuk mengecek nya :
```bash
sns.heatmap(df.isnull())
```
```bash
out :
```
![image](https://github.com/RohmatIF/Rohmat_ML/assets/147891420/b7208d42-826d-4035-873d-b01437dc54a6)
Data di atas terlihat aman 

Selanjutnya kita akan melihat gambaran visual tentang sejauh mana variable dalam DataFrame ini berkorelasi, kiata bisa menggunakan Heatmap untuk dapat melihatnya.
```bash
plt.figure(figsize=(24,10))
sns.heatmap(df.corr(),annot=True)
```
```bash
out :
```
![image](https://github.com/RohmatIF/Rohmat_ML/assets/147891420/b27e8a71-4d19-4f53-b5c7-1ed3eb55ff5a)

Kita juga dapat menganalisis variabel-variabel yang saling berhubungan, contohnya disini kita akan memaparkan beberapa subplot seperti Battery,RAM,Front_Camera dan Price_Range, kita akan mencoba Price_Range sebagai variabel independen dan bagaimana hubungannya dengan variable-variable lain.
```bash
plt.figure(figsize = (16,4))
plt.subplot(1,4,1)
sns.barplot(x = 'Price_Range', y = 'Battery', data = df, palette = 'Blues')
plt.subplot(1,4,2)
sns.barplot(x = 'Price_Range', y = 'RAM',data = df, palette = 'Blues')
plt.subplot(1,4,3)
sns.barplot(x = 'Price_Range', y = 'Front_Camera', data = df, palette = 'Blues')
plt.show()
```
```bash
out :
```
![image](https://github.com/RohmatIF/Rohmat_ML/assets/147891420/ab889eaa-a066-47d0-a210-030216e8547c)
Hal ini dapat membantu memahami bagaimana spesifikasi perangkat berubah atau berkorelasi dengan harga yang berbeda berdasarkan Price_Range

Selanjutnya kita juga dapat
```bash
out :
```
```bash
out :
```















