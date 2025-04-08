import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Web Application Cars")

# Cargar archivo csv limpio 
data_clean = pd.read_csv("C:/Users/Vane/Desktop/PracticasTripletenVane/06DataCars/Data/data_clean.csv")

# Subtítulo
st.subheader("Data Viewer")

st.write(data_clean.head())
