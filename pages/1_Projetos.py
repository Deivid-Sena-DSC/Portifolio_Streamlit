import streamlit as st
import json
from pages.Projetos.api_cep import consulta_cep
from pages.Projetos.api_coordenadas import localizar_coordenadas

if st.button("Voltar a Home Page"):
    st.switch_page("Home.py")

st.header('Página de Projetos.')

tab1, tab2 = st.tabs(['Consulta CEP','Outros'])

with tab1:
    cep = st.text_input('Digite o seu CEP:').strip()
    with st.spinner('CARREGANDO...'):        
        if cep:
            if "-" in cep:
                cep = cep.replace("-","")
            try:
                cep_final = json.loads(consulta_cep(cep))
                st.write(f'CEP: {cep_final['cep']}')
                st.write(f'Logradouro: {cep_final['logradouro']}')
                st.write(f'Bairro: {cep_final['bairro']}')
                st.write(f'Estado: {cep_final['localidade']}')
                st.write(f'UF: {cep_final['uf']}')

                st.plotly_chart(localizar_coordenadas(cep_final['bairro'], cep_final['localidade'], cep_final['uf'], cep_final['cep']))

            except:
                st.write('Desculpe CEP não encontrado tente novamente')