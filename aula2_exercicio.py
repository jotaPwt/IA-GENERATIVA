import streamlit as st # plotagem / 
import pandas as pd # leitura / dataframe


# st.title('Calculadora')



# n1 = st.number_input('Escolha um número')
# n2 = st.number_input('Escolha outro número')

# operacao = st.chat_input("""
#  - Escolha uma operação
              
#      +   -   /   *


# """)

# if st.button('RESTULTADO'):
#     soma = n1 + n2
#     st.success(soma)


# -----------------
    

# st.title("IMC")

# peso = st.number_input("n1")
# altura = st.number_input("n2")

# if st.button('Calcular IMC'):
#     calculo = round(peso / (altura ** 2), 2)
#     st.success(calculo)



# --------- escolha de atividade mao na massa: Cadastro Simples
    

st.title('CADASTRO SIMPLES')

nome = st.text_input('Digite seu primeiro nome')
ultimo_nome = st.text_input('Digite seu último nome')
email = st.text_input('digite seu e-mail')
idade = st.number_input('Digite sua idade')


if st.button("EXIBIR INFOS"):
    if nome and ultimo_nome:
        nome_completo = f"{nome} {ultimo_nome}"
        st.success(f'Seja bem vindo {nome_completo}, seu email é {email} e sua idade é {idade}')
        
    else:
        st.error("Por favor, preencha os dois campos.")