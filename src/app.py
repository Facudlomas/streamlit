import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache(ttl=60*5, max_entries=20)
def load_data():
    data = pd.read_csv('/workspaces/streamlit/data/decision_tree_classifier_default_42.sav')
    return data

data = load_data()

st.markdown('<style>description{color:green;}</style>', unsafe_allow_html=True)
st.title('prediccion de diabetes')
st.markdown("<description>con algunos parametros podemos predecir en si tiene posibilidad de tener diabetes </description>", unsafe_allow_html=True)
st.sidebar.title('Select')