import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar CSV desde Azure Blob Storage
csv_url = "https://trivyreportscan.blob.core.windows.net/cost-analysis/reports/cloud-cost-20250408.csv"

st.title("🌥️ Cloud Cost Dashboard")

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(csv_url)

st.subheader("Vista previa de los datos")
st.dataframe(df)

st.subheader("Gráfico de costos por servicio (Azure)")
if 'MeterCategory' in df.columns and 'PreTaxCost' in df.columns:
    azure_group = df.groupby("MeterCategory")["PreTaxCost"].sum().sort_values(ascending=False)
    st.bar_chart(azure_group)

st.subheader("Distribución de costos (Azure)")
if 'PreTaxCost' in df.columns:
    fig, ax = plt.subplots()
    df['PreTaxCost'].plot(kind='hist', bins=20, ax=ax)
    ax.set_xlabel("Costo (USD)")
    ax.set_title("Distribución de costos Azure")
    st.pyplot(fig)
