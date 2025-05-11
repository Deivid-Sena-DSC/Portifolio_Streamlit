import streamlit as st

if st.button("Voltar a Home Page"):
    st.switch_page("Home.py")

st.subheader('Sobre Mim e Contato.')

st.write(f"""Olá.\n\nAtualmente estou me desenvolvendo profissionalmente para atuar como Analista de Dados. Tenho experiência com Python, SQL, Excel avançado e Power BI, aplicando essas ferramentas para transformar dados em informações relevantes e apoiar a tomada de decisão.\n\nSou apaixonado por tecnologia e tenho forte interesse em automação de processos, análise de dados e desenvolvimento de soluções inteligentes. Trabalho com bibliotecas como Pandas para manipulação de dados, Selenium e PyAutoGUI para automações, além de Streamlit e Flask para criação de aplicações e dashboards interativos.\n\nEstou sempre buscando evoluir, aplicando boas práticas de ETL, data wrangling e visualização de dados. Aberto a novas oportunidades e desafios que me permitam crescer e gerar impacto com dados.""")

st.html('pages/contato.html')
