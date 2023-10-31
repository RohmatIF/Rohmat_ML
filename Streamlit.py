import pickle
import streamlit as st

model = pickle.load(open('estimasi_Mobile_2023.sav', 'rb'))

st.title('Estimasi Harga smartphone 2023')
st.markdown('---')

brand_options = {
    0: "Apple",
    1: "Asus",
    2: "Google",
    3: "Infinix",
    4: "Xiomi",
    5: "Motorola",
    6: "OnePlus",
    7: "OPPO",
    8: "POCO",
    9: "Realme",
    10: "Redmi",
    11: "SAMSUNG",
    12: "Tecno",
    13: "vivo"
}

brand_mode = st.checkbox("Pilih Brand Berdasarkan Nama", value=False)

if brand_mode:
    BrandCategory = st.selectbox('Pilih kategori Brand', list(brand_options.values()))
else:
    BrandCategory = st.selectbox('Pilih kategori Brand', list(brand_options.keys()))

processor_options = {
    0: "Apple",
    1: "Exynos",
    2: "Google Tensor",
    3: "Intel",
    4: "MediaTek",
    5: "Snapdragon",
    6: "Unisoc"
}

processor_mode = st.checkbox("Pilih Processor Berdasarkan Nama", value=False)

if processor_mode:
    ProcessorCategory = st.selectbox('Inputkan', list(processor_options.values()))
else:
    ProcessorCategory = st.selectbox('Inputkan', list(processor_options.keys()))


ram_options = [1, 2, 3, 4, 6, 8, 12, 16, 18]
RAM = st.selectbox('Pilih RAM (In GB)', ram_options)


rom_options = [2, 8, 12, 16, 25, 32, 64, 128, 256, 512, 1024]
ROM = st.selectbox('Pilih ROM (In GB)', rom_options)

Battery = st.selectbox('Input Kapasitas Batrai mAh', ('3000', '3500', '4000', '4500', '5000'))
Diplay_Size = st.slider('Input Ukuran layar', 200, 600, 50)
Front_Camera = st.slider('Input spesifikasi kamera depan Mega Px', 5, 100, 5)
Back_Camera = st.slider('Input spesifikasi kamera belakang Mega Px', 5, 100, 5)

predict = ''

if st.button('Estimasi Harga'):
    if brand_mode:
        BrandCategory = [key for key, value in brand_options.items() if value == BrandCategory][0]
    if processor_mode:
        processor_category = [key for key, value in processor_options.items() if value == ProcessorCategory][0]
    else:
        processor_category = ProcessorCategory
    predict = model.predict(
        [[float(BrandCategory), float(processor_category), float(RAM), float(ROM), float(Battery), float(Diplay_Size), float(Back_Camera), float(Front_Camera)]]
    )
    st.write('Prediksi Harga Smartphone (Rupiah): ', predict*1)
