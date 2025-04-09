
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cloud Cost Dashboard", layout="wide")

st.title("☁️ Cloud Cost Report")

# Cargar el archivo CSV
csv_path = "cloud-cost-sample.csv"
df = pd.read_csv(csv_path)

# Mostrar tabla
st.subheader("📄 Raw Cost Data")
st.dataframe(df)

# Gráfica de barras de comparación
st.subheader("📊 Weekly Cost Comparison")
fig, ax = plt.subplots()
df_grouped = df.groupby("Cloud")["Cost"].sum()
df_grouped.plot(kind="bar", ax=ax, color=["#007FFF", "#FF9900"])
ax.set_ylabel("USD")
ax.set_title("Weekly Cloud Spend")
st.pyplot(fig)
