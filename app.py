import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
st.header('Data Viewer')

hist_button = st.button('Construir un histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_dispertion = st.checkbox('Construir grafico de dispersion')

if build_dispertion:
    st.write('Creación de un gráfico de disperión para el conjunto de datos de anuncios de venta de coches ')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
