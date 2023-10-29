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

### Variable-variable pada Dataset Mobile Price Data 2023 adalah sebagai berikut
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

Hubungkan dengan Kaggle lalu input Datasets dari kaggle



