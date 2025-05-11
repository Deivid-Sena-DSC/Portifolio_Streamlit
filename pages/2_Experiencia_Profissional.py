import streamlit as st

if st.button("Voltar a Home Page"):
    st.switch_page("Home.py")

st.subheader('Experiência Profissional.')

st.subheader("Contax SA.")
with st.expander("Click para expandir", expanded=False):
        st.image(r"pages/imagens/contax.png")
        st.write('Analista de Remuneração.')
        st.write("Data de início: 12/2024")
        st.write("Data de saída: 03/2025")
        st.write(f"""Análise de desempenho de campanhas de vendas, com cálculo de resultados e indicadores em Excel, incluindo taxa de conversão e alcance.\nAutomação de processos de cadastro e coleta de dados utilizando Selenium, otimizando rotinas repetitivas e reduzindo falhas.\nExecução de ETL (extração, transformação e carga) de dados a partir de planilhas, utilizando Python para estruturação e análise de dados.\nCalibração e acompanhamento de metas operacionais, com base em análises comparativas e projeções.\nDesenvolvimento de dashboards interativos e acompanhamento de KPIs com foco em performance e tomada de decisão.\nParticipação ativa em reuniões estratégicas, contribuindo com insights orientados por dados para embasar decisões gerenciais.""")

st.subheader("Viação Grajaú SA.")
with st.expander("Click para expandir", expanded=False):
        st.image(r"pages/imagens/viacaograjau.png")
        st.write('Cargo: Assistende de centro de operações da concessionária.')
        st.write("Data de início: 04/2022")
        st.write("Data de saída: 06/2024")
        st.write(f"""Monitoramento e rastreamento de veículos e operações em tempo real, com foco na segurança e eficiência operacional.\nSuporte ao Centro de Controle Operacional (CCO) da concessionária, atuando diretamente no acompanhamento das ocorrências.\nElaboração e atualização de relatórios operacionais e planilhas analíticas no Excel.\nAtendimento telefônico e orientação a fiscais e operadores de campo, garantindo comunicação eficaz e resolução ágil de problemas.\nUtilização de sistemas de telemetria e plataformas de monitoramento para coleta e análise de dados operacionais.""")

st.subheader("CNB Serviços de Inventário.")
with st.expander("Click para expandir", expanded=False):
        st.image(r"pages/imagens/cnb.png")
        st.write('Cargo: Inventariante.')
        st.write("Data de início: 09/2020")
        st.write("Data de saída: 04/2022")
        st.write(f"""Separação, conferência, embalagem e distribuição de produtos, assegurando a integridade e o correto envio dos itens.\nOrganização e contagem de estoque, com controle de entradas e saídas para garantir acuracidade.\nRecebimento e conferência de notas fiscais, com estocagem adequada das mercadorias conforme tipo e categoria.\nAtualização e controle de estoque por meio de planilhas em Excel, contribuindo para o gerenciamento eficiente do inventário.\nParticipação em processos de carga e descarga de contêineres, seguindo normas de segurança e logística.""")

st.subheader("Socicam Administração Projetos e Representações LTDA.")
with st.expander("Click para expandir", expanded=False):
        st.image(r"pages/imagens/socicam.png")
        st.write('Cargo: Agente de Terminal Urbano.')
        st.write("Data de início: 02/2015")
        st.write("Data de saída: 07/2019")
        st.write(f"""Atendimento e orientação a usuários do terminal, incluindo suporte e condução de pessoas com deficiência (PCD), garantindo acessibilidade e segurança.\nAdministração geral do terminal, com elaboração de relatórios operacionais diários em livro físico e digital.\nComunicação via e-mail com setores internos e externos para solicitação e acompanhamento de manutenções preventivas e corretivas.\nUtilização de códigos Q e procedimentos operacionais padronizados para comunicação e registros.\nMonitoramento de segurança por meio de CFTV (circuito fechado de TV).\nRastreamento e monitoramento de veículos em tempo real via sistema integrado com GPS""")