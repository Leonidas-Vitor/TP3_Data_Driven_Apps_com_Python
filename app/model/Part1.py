import streamlit as st
import numpy as np
from services import GeminiConfig as gc
import tiktoken as tk
import requests
#from bs4 import BeautifulSoup
import plotly.graph_objects as go
import json
import pandas as pd
import yaml

st.header('Parte 1 - Conceituação do projeto')

#with st.spinner('Carregando configurações...'):
#    config = tk.GetConfig()
#    model = gc.GetGeminiModel(config)

@st.cache_data
def GetGeminiResponse(config : dict, prompt : str):
    model = gc.GetGeminiModel(config)
    response = model.generate_content(prompt)
    return response