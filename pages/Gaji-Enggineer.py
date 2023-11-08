import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Salinan salaries.csv")

# Tampilkan data teratas
st.header("Data Gaji Karyawan")
st.write("Data gaji karyawan:")
st.table(data.head(10))

# Hitung rata-rata gaji
rata_rata_gaji = data["salary"].dropna().mean()

st.write("Rata-rata gaji:", rata_rata_gaji, "juta")

import streamlit as st
import matplotlib.pyplot as plt

# Data
data = {
    "Jabatan": ["Manager", "Staff", "Supervisor"],
    "Jumlah": [3, 5, 2],
}

# Plot
plt.pie(data["Jumlah"], labels=data["Jabatan"], colors=["#FF0000", "#00FF00", "#0000FF"], explode=[0.1, 0, 0])

# Tampilkan plot
st.pyplot(plt)

st.write("Berikut adalah data karyawan perposisi")
import numpy as np

# Load dataset
data = np.loadtxt("Salinan salaries.csv", dtype=str, delimiter=",")

# Hitung jumlah karyawan perposisi
jumlah_karyawanperposisi = np.unique(data[:, 1], return_counts=True)

# Tampilkan hasil
st.table(jumlah_karyawanperposisi)

import pandas as pd

st.write("Berikut adalah data gaji karyawan perposisi")
# Load dataset
data = pd.read_csv("Salinan salaries.csv")

# Load dataset
data = pd.read_csv("Salinan salaries.csv")

# Hitung rata-rata gaji per posisi
rata_rata_gajiperposisi = data.groupby("job_title")["salary"].mean().to_frame()

# Tampilkan hasil
st.table(rata_rata_gajiperposisi)

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Salinan salaries.csv")

# Hitung rata-rata gaji per posisi
rata_rata_gaji_perposisi = data.groupby("job_title")["salary"].mean()

# Buat grafik
plt.pie(rata_rata_gaji_perposisi.values, labels=rata_rata_gaji_perposisi.index, autopct="%.2f%%")
plt.title("Rata-rata Gaji Pegawai Per Posisi")

# Tampilkan grafik di Streamlit
st.pyplot(plt.gcf())
