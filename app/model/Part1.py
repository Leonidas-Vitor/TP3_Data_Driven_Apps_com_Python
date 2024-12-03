import streamlit as st

st.header('Parte 1 - Conceituação do projeto')

st.subheader('Problema',divider=True)

st.write('''
    O mercado financeiro é um ambiente complexo e dinâmico, onde a tomada de decisão é baseada em informações e análises
    de dados. A quantidade de informações disponíveis é vasta e pode ser difícil para um investidor iniciante
    ou mesmo para um investidor experiente, acompanhar todas as tendências e informações relevantes para a tomada de decisão.
    A falta de informações ou a análise incorreta de dados pode levar a prejuízos financeiros.
    ''')

st.subheader('Solução',divider=True)
st.write('''
        A aplicação de agentes inteligentes irá auxiliar o investidor a tomar decisões mais assertivas no mercado financeiro.
        Através de buscas de tendências e condições atuais do mercado, o agente irá fornecer informações relevantes para o investidor.
        ''')

st.write('''**Recursos do chatbot:**''')
st.write('''
    - Acesso ao Google
    - Acesso ao Google Finance
    - Acesso ao Google Trends
    - Histórico de conversas
    ''')

st.subheader('Exemplos de aplicação',divider=True)
st.write('''
    - Saber mais sobre uma empresa específica
    - Saber como um determinado setor está se comportando no mercado
    - Resumir notícias e/ou fatos relevantes de uma empresa
    ''')

st.subheader('Objetivo',divider=True)
st.write(
    '''
    Ter um chatbot com implementação de agentes inteligentes que possa auxiliar o investidor a tomar decisões mais assertivas no mercado financeiro 
    e ser implementado no projeto de bloco de Ciência de Dados Aplicada, afim de enriquecer a geração de relatórios.
    ''')


st.subheader('Especificações',divider=True)
st.markdown(
    '''
    |   Especificação   |   Descrição   |
    |-------------------|---------------|
    |   Linguagem       |   Python      |
    |   Framework       |   Streamlit   |
    |   LLM             |   Gemini      |
    '''
)

st.subheader('Problemas conhecidos',divider=True)
st.write(
    '''
    - Erro exporádico de índice de liste "langchain\chains\base.py", line 516
    - Erro exporádico em "langchain_community\utilities\google_finance.py", line 79
    '''
)