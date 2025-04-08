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


# Procesar los datos para el conteo
vehicle_counts = data_clean.groupby(["manufacturer", "type"]).size().reset_index(name="count")

# Crear el gráfico de barras
fig = px.bar(
    vehicle_counts,
    x="manufacturer",
    y="count",
    color="type",
    title="Tipos de vehículos por fabricante",
    labels={"manufacturer": "Fabricante", "count": "Cantidad de vehículos", "type": "Tipo de vehículo"},
    barmode="stack"  # Apila las barras por tipo
)

# Configurar la visualización en Streamlit
st.title("Gráfico de Tipos de Vehículos por Fabricante")
st.plotly_chart(fig)


# Filtrar los registros con año 0 en la columna model_year
data_filtered = data_clean[data_clean["model_year"] > 0]

# Crear un histograma con los datos filtrados
fig = px.histogram(
    data_filtered,
    x="model_year",
    color="condition",
    title="Distribución de vehículos por condición y año modelo ",
    labels={"model_year": "Año modelo", "condition": "Condición del vehículo"},
    barmode="group"  # Agrupar las barras por condición
)

# Configurar Streamlit
st.title("Histograma ajustado: Condición vs Año modelo")
st.write("Este gráfico excluye los registros con año 0 para mejorar la distribución visual.")

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)


# data_clean = pd.read_csv("data_clean.csv")

# Título de la aplicación
st.title("Comparar la distribución de precios entre fabricantes")

# Menús desplegables para seleccionar tres fabricantes
manufacturer_1 = st.selectbox("Selecciona el fabricante 1:", data_clean["manufacturer"].unique())
manufacturer_2 = st.selectbox("Selecciona el fabricante 2:", data_clean["manufacturer"].unique())
manufacturer_3 = st.selectbox("Selecciona el fabricante 3:", data_clean["manufacturer"].unique())

# Filtrar los datos para incluir solo los fabricantes seleccionados
filtered_data = data_clean[data_clean["manufacturer"].isin([manufacturer_1, manufacturer_2, manufacturer_3])]

# Crear el histograma con Plotly
fig = px.histogram(
    filtered_data,
    x="price",
    color="manufacturer",
    title="Distribución de precios por fabricante",
    labels={"price": "Precio", "manufacturer": "Fabricante"},
    barmode="overlay",  # Las barras se superponen
    histnorm="percent"  # Normalización a porcentaje
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)