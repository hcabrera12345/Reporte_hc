import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Reporte de Análisis GES y DOS", layout="wide", initial_sidebar_state="collapsed")

html_file = "analisis_completo.html"

if os.path.exists(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_data = f.read()
    
    # Renderizamos el HTML directamente en Streamlit cubriendo toda la pantalla
    components.html(html_data, height=3500, scrolling=True)
else:
    st.error(f"El archivo {html_file} no se encontró en el servidor.")
    st.info("Asegúrate de ejecutar primero el script 'analisis_pandas_completo_1.py' para generar el HTML.")
