import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

X = dados_vendas[['investimento']]
y = dados_vendas['faturamento']

modelo = LinearRegression()
modelo.fit(X, y)

investimento_usuario = st.number_input("Digite o valor do investimento:", min_value=0)

if st.button("Prever"):
    entrada = pd.DataFrame([[investimento_usuario]], columns=['investimento'])
    previsao = modelo.predict(entrada)
    st.write(f"Faturamento previsto: R$ {previsao[0]:.2f}")
