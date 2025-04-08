import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Web Application Cars")

# Cargar archivo csv limpio 
data_clean = pd.read_csv("C:/Users/Vane/Desktop/PracticasTripletenVane/06DataCars/Data/data_clean.csv")

# Subtítulo
st.subheader("Data Viewer")

  
# Contar la cantidad de anuncios por fabricante
ads_by_manufacturer = data_clean['manufacturer'].value_counts()

# Checkbox para incluir fabricantes con menos de 1000 anuncios
include_less_than_1000 = st.checkbox("Incluir fabricantes con menos de 1000 anuncios")

# Filtrar fabricantes si el checkbox está activado
if include_less_than_1000:
    manufacturers_filtered = ads_by_manufacturer[ads_by_manufacturer < 1000].index
    data_filtered = data_clean[data_clean['manufacturer'].isin(manufacturers_filtered)]
else:
    data_filtered = data_clean

st.dataframe(data_filtered)

