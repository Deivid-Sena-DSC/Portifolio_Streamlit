import requests
import streamlit as st

#BUSCAR CEP
def consulta_cep(cep):
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    resultado_cep = requests.get(url)
    return resultado_cep.text


#BUSCAR CNPJ
def consulta_cnpj(cnpj):
    url = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}'
    resultado_cnpj = requests.get(url)
    return resultado_cnpj.text

#BUSCAR FIBE
def consulta_fibe(fibe):
    url = f'https://brasilapi.com.br/api/fipe/preco/v1/{fibe}'
    resultado_fibe = requests.get(url)
    return resultado_fibe.text


#FUNÇÃO PARA CARREGAR O CÓDIGO DA API
def brasil_api():
    st.write('Aqui eu ultilizo a BrasilAPI para buscar informações sobre CEP, CNPJ e TABELA FIBE')

    if 'show_cep' not in st.session_state:
        st.session_state['show_cep'] = False
    if 'show_cnpj' not in st.session_state:
        st.session_state['show_cnpj'] = False
    if 'show_fibe' not in st.session_state:
        st.session_state['show_fibe'] = False  

    cep_col, cnpj_col, fipe_col = st.columns(3)


    with cep_col:
        if st.button('CEP'):
            st.session_state['show_cep'] = not st.session_state['show_cep']
        
        if st.session_state['show_cep']:
            cep_texto = st.text_input('Digite o CEP').strip()
            botao_buscar_cep = st.button('Buscar CEP')
            try:
                if cep_texto and botao_buscar_cep:
                    resultado_cep = json.loads(consulta_cep(cep_texto))
                    for chave, valor in resultado_cep.items():
                        try:
                            st.write(chave, ' : ', valor)
                        except:
                            st.write(chave, ' Sem informação')
            except:
                st.write('Não foi possivel buscar o CEP informado verifique se a informação está correta')



    with cnpj_col:    
        if st.button('CNPJ'):
            st.session_state['show_cnpj'] = not st.session_state['show_cnpj']
        
        if st.session_state['show_cnpj']:
            cnpj_texto = st.text_input('Digite o CNPJ').strip()    
            botao_buscar_cnpj = st.button('Buscar CNPJ')
            try:
                if cnpj_texto and botao_buscar_cnpj:
                    resultado_cnpj = json.loads(consulta_cnpj(cnpj_texto))
                    for chave, valor in resultado_cnpj.items():
                        try:
                            st.write(chave, " : ", valor  )
                        except:
                            st.write(chave, ' Sem informação')
            except:
                st.write('Não foi possivel buscar o CNPJ informado verifique se a informação está correta')



        
    with fipe_col:    
        if st.button('Tabela Fibe'):
            st.session_state['show_fibe'] = not st.session_state['show_fibe']

        if st.session_state['show_fibe']:
            fibe_texto = st.text_input('Digite o número da Fibe')
            botao_buscar_fibe = st.button('Buscar Fibe')
            try:
                if fibe_texto and botao_buscar_fibe:
                    resultado_fibe = json.loads(consulta_fibe(fibe_texto))
                    for chave, valor in resultado_fibe.items():
                        try:
                            st.write(chave, " : ", valor)
                        except:
                            st.write(chave, ' Sem informação')
            except:
                st.write('Não foi possivel buscar o número FIBE informado verifique se a informação está correta')