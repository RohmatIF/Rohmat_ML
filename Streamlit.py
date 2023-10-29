import pickle
import streamlit as st

model = pickle.load(open('estimasi_Mobile_2023.sav', 'rb'))

st.title('Estimasi Harga smartphone 2023')

BrandCategory = st.selectbox('Pilih kategori Brand', list(range(1, 14)))

processor_options = {
    0: "Apple",
    1: "Exynos",
    2: "Google Tensor",
    3: "Intel",
    4: "MediaTek",
    5: "Snapdragon",
    6: "Unisoc"
}

processor_mode = st.checkbox("Pilih Kategori Berdasarkan Nama", value=False)

if processor_mode:
    ProcessorCategory = st.selectbox('Inputkan', list(processor_options.values()))
else:
    ProcessorCategory = st.selectbox('Inputkan', list(processor_options.keys()))

# Dropdown untuk RAM
ram_options = [1, 2, 3, 4, 6, 8, 12, 16, 18]
RAM = st.selectbox('Pilih RAM', ram_options)

# Dropdown untuk ROM
rom_options = [2, 8, 12, 16, 25, 32, 64, 128, 256, 512, 1024]
ROM = st.selectbox('Pilih ROM', rom_options)

Battery = st.number_input('Input Kapasitas Batrai (mAh)')
Diplay_Size = st.number_input('Input Ukuran layar')
Front_Camera = st.number_input('Input spesifikasi kamera depan (Mega Px)')
Back_Camera = st.number_input('Input spesifikasi kamera belakang (Mega Px)')

predict = ''

if st.button('Estimasi Harga'):
    if processor_mode:
        processor_category = [key for key, value in processor_options.items() if value == ProcessorCategory][0]
    else:
        processor_category = ProcessorCategory
    predict = model.predict(
        [[BrandCategory, processor_category, RAM, ROM, Battery, Diplay_Size, Back_Camera, Front_Camera]]
    )
    st.write('Estimasi harga mobile Phone 2023 dalam Ponds:', predict)
    st.write('Estimasi harga mobile Phone 2023 IDR (Juta):', predict * 19000)
