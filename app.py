import streamlit as st
import pandas as pd

# Usuários e senhas
usuarios = {
    "admin": "1234",
    "usuario": "senha"
}

# Inicializa o estado de login se ainda não existir
if "logado" not in st.session_state:
    st.session_state.logado = False
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

st.title("🎯 Plataforma de Loterias")

# Se o usuário ainda não estiver logado
if not st.session_state.logado:
    st.subheader("🔐 Login")
    user = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if user in usuarios and usuarios[user] == senha:
            st.session_state.logado = True
            st.session_state.usuario = user
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
else:
    st.success(f"Bem-vindo, {st.session_state.usuario}!")

    # Botão de logout
    if st.button("Sair"):
        st.session_state.logado = False
        st.session_state.usuario = ""
        st.rerun()

    st.subheader("📁 Importar Arquivo .txt")
    arquivo = st.file_uploader("Escolha um arquivo", type=["txt"])

    if arquivo is not None:
        # Leitura do conteúdo
        conteudo = arquivo.read().decode("utf-8")
        linhas = conteudo.strip().splitlines()
        dados = [linha.split(",") for linha in linhas]
        df = pd.DataFrame(dados)

        st.write("📋 Conteúdo do arquivo:")
        st.dataframe(df)
