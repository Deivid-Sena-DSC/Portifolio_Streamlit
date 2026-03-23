import streamlit as st
import json
from pages.Projetos.brasil_api import brasil_api
from pages.Projetos.api_coordenadas import localizar_coordenadas

if st.button("Voltar a Home Page"):
    st.switch_page("Home.py")

st.header('Página de Projetos.')

tab1, tab2 = st.tabs(['BRASIL API','Outros'])

with tab1:
    brasil_api()