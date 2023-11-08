import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data_rice = pd.read_csv("Salinan Rice Production Indonesia 2020-2022.csv")
data_salary = pd.read_csv("Salinan salaries.csv")
data_trend = pd.read_csv("shopping_trends_updated.csv")

# Tampilkan data
st.title("Analisis Data")
st.write("Berikut adalah data yang akan dianalisis:")
st.write("* Produksi beras di Indonesia ")
st.write("* Gaji karyawan di sebuah perusahaan")
st.write("* Tren belanja online ")
st.write("Kelompok : ")
st.write("* Hamzah Pratama Akbar")
st.write("* Fattah Satrio Atmojo")
st.write("* Reza Maulana Akbar")
st.write("* Muhammad Abdul Harits")


