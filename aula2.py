import streamlit as st
import pandas as pd 


st.title('isso é um titulo')
st.button('clique aqui')
st.write('Isso é paragrafo')
dados = {
'vendas':[100,20,30,60],
'mês':['jan','fev','mar','abril']
}


df =  pd.DataFrame(dados)
st.line_chart(df, x='mês', y='vendas')

# depurar 


st.title('isso é um titulo')
st.write('Isso é paragrafo')





dados = {
'vendas':[100,20,30,60],
'mês':['jan','fev','mar','abril']
}



if st.button('clique aqui'):
    d = pd.read_csv('dados.csv')
    df =  pd.DataFrame(d)


    st.bar_chart(df, x='mes', y='vendas')
    st.scatter_chart(df, x='mes', y='vendas')
    
    st.title('❤️')