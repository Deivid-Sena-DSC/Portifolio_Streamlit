import streamlit as st
from time import sleep

def home_page():
    st.set_page_config(
        page_title="Home",
        page_icon=":house:",
        layout="wide",
        initial_sidebar_state="collapsed")

    st.subheader("Olá me chamo Deivid S.C. Caldas, obrigado por acessar meu portifólio.")
    mensagens_ia = ["Digite o número de uma das opções abaixo e você será redirecionado automaticamente para a página da opção desejada.",
                    "1 - Página de Projetos.",
                    "2 - Experiencia Profissional.",
                    "3 - Formação Academica.",
                    "4 - Mais sobre mim e contato."] 
    for mensagem in mensagens_ia:
        with st.chat_message('ai'):    
            st.write(mensagem)

    mensagem_usuario = st.chat_input("Digite sua mensagem")
    if mensagem_usuario:
        if 'mensagens' in st.session_state:
            mensagens = st.session_state["mensagens"]
        else:
            mensagens = []
            st.session_state["mensagens"] = mensagens

        mensagens.append({"usuario": "user" , "texto" : mensagem_usuario.strip()})

        for mensagen in mensagens:
            with st.chat_message(mensagen['usuario']):
                st.write(mensagen['texto'])
        
        if mensagens[-1]["texto"] == '1':
            with st.chat_message('ai'):    
                st.write(f'Ok, Redirecionando para {mensagens_ia[1]}')
                sleep(2)
                st.switch_page("pages/1_Projetos.py")

        elif mensagens[-1]["texto"] == '2':
            with st.chat_message('ai'):    
                st.write(f'Ok, Redirecionando para {mensagens_ia[2]}')
                sleep(2)
                st.switch_page("pages/2_Experiencia_Profissional.py")

        elif mensagens[-1]["texto"] == '3':
            with st.chat_message('ai'):    
                st.write(f'Ok, Redirecionando para {mensagens_ia[3]}')
                sleep(2)
                st.switch_page("pages/3_Formacao_Academica.py")

        elif mensagens[-1]["texto"] == '4':
            with st.chat_message('ai'):    
                st.write(f'Ok, Redirecionando para {mensagens_ia[4]}')
                sleep(2)
                st.switch_page("pages/4_Sobre_Mim_e_Contato.py")
        else:
            with st.chat_message('ai'):    
                st.write(f'Desculpe!\nNão tem a opção desejada')
                
if __name__ == "__main__":
    home_page()