import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Data Preparation
data = pd.read_csv("shopping_trends_updated.csv")

# Data Analysis
pendapatan_per_kategori = data.groupby("Category")["Purchase Amount (USD)"].sum()
pendapatan_per_bulan = data.groupby("Season")["Purchase Amount (USD)"].sum()
peningkatan_pendapatan = pendapatan_per_bulan.diff()

# Data Visualization
fig_pendapatan_per_kategori = plt.figure(figsize=(10, 6))
plt.bar(pendapatan_per_kategori.index, pendapatan_per_kategori.values)
plt.xlabel("Kategori")
plt.ylabel("Pendapatan")
plt.title("Pendapatan per Kategori")

fig_pendapatan_per_bulan = plt.figure(figsize=(10, 6))
plt.plot(pendapatan_per_bulan.index, pendapatan_per_bulan.values)
plt.xlabel("Tanggal")
plt.ylabel("Pendapatan")
plt.title("Pendapatan per Bulan")

fig_peningkatan_pendapatan = plt.figure(figsize=(10, 6))
plt.plot(peningkatan_pendapatan.index, peningkatan_pendapatan.values)
plt.xlabel("Tanggal")
plt.ylabel("Peningkatan Pendapatan")
plt.title("Peningkatan Pendapatan")

# Display the graphs
with st.container():
    st.title("Data Analisis Belanja")

    st.subheader("Pendapatan per Kategori")
    st.plotly_chart(fig_pendapatan_per_kategori)

    st.subheader("Pendapatan per Bulan")
    st.plotly_chart(fig_pendapatan_per_bulan)

    st.subheader("Peningkatan Pendapatan")
    st.plotly_chart(fig_peningkatan_pendapatan)
