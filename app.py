import streamlit as st 
import pandas as pd 
import plotly_express as px 

car_data = pd.read_csv('C:/Users/User/OneDrive/Data Analyst/GitHub/quinto_proyecto_da/vehicles_us.csv')
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True) 
