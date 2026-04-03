import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Reporte de Análisis GES y DOS", layout="wide", initial_sidebar_state="collapsed")

html_file = "analisis_completo.html"
html_file_alt = "index.html"

if os.path.exists(html_file):
    archivo_a_leer = html_file
elif os.path.exists(html_file_alt):
    archivo_a_leer = html_file_alt
else:
    archivo_a_leer = None

if archivo_a_leer:
    with open(archivo_a_leer, 'r', encoding='utf-8') as f:
        html_data = f.read()
    
    # Renderizamos el HTML directamente en Streamlit cubriendo toda la pantalla
    components.html(html_data, height=3500, scrolling=True)
else:
    st.error(f"El archivo no se encontró en el servidor de GitHub.")
