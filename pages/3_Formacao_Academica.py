import streamlit as st

if st.button("Voltar a Home Page"):
    st.switch_page("Home.py")

st.subheader('Formação Acadêmica.')

st.subheader("Excel Completo.")
with st.expander("Click para expandir", expanded=False):
        st.image(r"pages/imagens/hashtag.png")
        st.write("Data de início: 12/2024 até 02/2025 duração 110 horas.")
        st.write(f"""Planilhas, Tabelas dinâmicas, Funções como PROCV, PROCX, PROCH, ÍNDICE(CORRESP), DATADIF, SOMASE, CONTSES, SEERRO, etc..\nPower Query, Formatação condicional, Validação de dados Funções financeiras VL, VP, PGTO, TAXA, VPL etc...\nPower Pivot, relacionamento entre tabelas, Google Sheets, Previsão Solver.""")
        st.link_button('Exibir Credencial', url='https://portalhashtag.com/certificado-hashtag/1739811653374x292463388337635300')
       
st.subheader("Power BI.")
with st.expander("Click para expandir", expanded=False):
        st.image(r"pages/imagens/senai.png")
        st.write("Data de início: 09/2024 até 11/2024 duração 40 horas.")
        st.write("Competências: Dashboard, Relatórios e análises, Microsoft Power Query, Indicadores chave de desempenho KPI's, DAX, modelagem de dados.")
        st.link_button('Exibir Credencial', url='https://www.sp.senai.br/consulta-certificado?qrcode=11524286163/14731259')
        
st.subheader("Análise de dados em nuvem  Microsoft DP-900.")
with st.expander("Click para expandir", expanded=False):
        st.image(r"pages/imagens/senai.png")
        st.write("Data de início: 09/2024 até 10/2024 duração 40 horas")
        st.write("Competências: Windows Azure, Azure Data Factory, Azure DataLake, Azure Functions, Azure Cosmos DB, Máquina Virtual, Azure Databricks, SQL Azure.")
        st.link_button('Exibir Credencial', url='https://www.sp.senai.br/consulta-certificado?qrcode=11224228029/14774805')
        
st.subheader("Python para Data Science.")
with st.expander("Click para expandir", expanded=False):
        st.image(r"pages/imagens/senai.png")
        st.write("Data de início: 08/2024 até 09/2024 duração 60 horas")
        st.write("Competências: Análises Descritiva, Diagnóstica, Preditiva, Prescritiva. Python bibliotecas Pandas, Matplotlib, Seaborn, Numpy, Datetime, Aed. Correlação, Modelos quantitativos, Árvore de decisão, Regressão linear, Manipulação e Transformação de Dados, Análise de cluster.")
        st.link_button('Exibir Credencial', url='https://www.sp.senai.br/consulta-certificado?qrcode=11224224032/14707349')

st.subheader("Programação em Python")
with st.expander("Click para expandir", expanded=False):
        st.image(r"pages/imagens/senai.png")
        st.write("Data de início: 07/2024 até 08/2024 duração 60 horas")
        st.write(f"Competências: Identificar os requisitos do problema para definição dos recursos a serem utilizados, Elaborar algoritmo da solução do problema, Configurar o ambiente de desenvolvimento em Python, Programar em linguagem Python, Programar jogos 2D em linguagem Python, Validar software por meio de testes")
        st.link_button('Exibir Credencial', url='https://www.sp.senai.br/consulta-certificado?qrcode=11524284892/14637258')