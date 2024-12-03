import streamlit as st
import numpy as np
from services import CustomTools as ct
import tiktoken as tk
import requests
#from bs4 import BeautifulSoup
import plotly.graph_objects as go
import json
import pandas as pd
import yaml
from services import Agent
from langchain_community.callbacks.streamlit import (
    StreamlitCallbackHandler,
)

from services.Memory import MEMORY

with st.spinner('Carregando aplicação...'):
    agent_chain = Agent.load_agent(MEMORY)

avatars = {
    "human": "user",
    "ai": "assistant"
}

def WriteHistory(messages):
    '''
    Escreve o histórico de mensagens
    '''
    try:
        #for history in st.session_state[memoryKey]:
            #role = 'Usuário' if 'Usuário' in history else 'Assistente'
            #icon = 'user' if 'Usuário' in history else 'assistant'
            #icon = entities[history['Role']]
            #messages.chat_message(icon).write(history['Msg'])
        for msg in MEMORY.chat_memory.messages:
            messages.chat_message(avatars[msg.type]).write(msg.content)
    except Exception as e:
        st.error(e)
        st.error('Erro ao escrever histórico')
        pass

def HistorySize():
    '''
    Retorna o tamanho do histórico
    '''
    user_count = 0
    for msg in MEMORY.chat_memory.messages:
        if msg.type == 'human':
            user_count += 1
    return user_count

#---------------------------------------------------Aplicação

st.header('Chat com especialidade em condições de mercado')


with st.container():  

    cols = st.columns([0.8,0.2])
    with cols[0]:
        messages = st.container(height=450)
        WriteHistory(messages)
        if HistorySize() < 3:
            if prompt := st.chat_input("Converse com o especialista de mercado", key='chat_input'):
                messages.chat_message("user").write(prompt)
                st.subheader('Pensamento do especialista',divider=True)
                with st.chat_message("assistant"):
                    st_callback = StreamlitCallbackHandler(st.container())
                    try:
                        response = agent_chain.invoke(
                            {"input": prompt},
                            {"callbacks": [st_callback]}
                        )
                        messages.chat_message("assistant").write(f"Assistente: {response['output']}")
                    except Exception as e:
                        st.error(f"Erro: {e}")
        else:
            st.write('Limite atingido, reinicia o chat para continuar')
    with cols[1]:
        st.write('Esse chat tem o limite de 3 interações, ao atingir o limite, reinicie o chat para continuar')
        st.write(f'Interações: {HistorySize()}/3')

        if st.button('Reiniciar'):
            #st.session_state[memoryKey].clear()
            MEMORY.clear()
            st.rerun()

        if HistorySize() == 3:
            st.warning('Limite atingido, reinicia o chat para continuar')
st.subheader('Memória', divider=True)
st.write(MEMORY.chat_memory.messages)
#st.write(MEMORY.list(config = {"configurable": {"thread_id": "abc123"}}))