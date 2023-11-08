import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Salinan Rice Production Indonesia 2020-2022.csv")

# Tampilkan data
st.title("Produksi Beras Indonesia")
st.write("Data produksi beras di Indonesia selama 3 tahun, dari tahun 2020 hingga 2022")
st.table(data)

# Buat plot produksi beras
plt.plot(data["Year"], data["Production.(ton)"])
plt.xlabel("Year")
plt.ylabel("Production.(ton)")
st.pyplot(plt)

# Hitung pertumbuhan produksi beras
pertumbuhan = (data["Production.(ton)"][2] - data["Production.(ton)"][0]) / data["Production.(ton)"][0] * 100
st.write("Pertumbuhan produksi beras selama 3 tahun:", pertumbuhan, "%")

# Tampilkan pilihan filter data
st.header("Filter Data")
tahun_awal = st.slider("Year awal", 2020, 2022, 2020)
tahun_akhir = st.slider("Year akhir", 2020, 2022, 2022)

# Filter data berdasarkan tahun
data_filter = data[data["Year"].between(tahun_awal, tahun_akhir)]

# Tampilkan data yang telah difilter
st.write("Data produksi beras di Indonesia selama", tahun_awal, "hingga", tahun_akhir)
st.table(data_filter)

# Buat plot produksi beras yang telah difilter
plt.plot(data_filter["Year"], data_filter["Production.(ton)"])
plt.xlabel("Year")
plt.ylabel("Production.(ton)")
st.pyplot(plt)

