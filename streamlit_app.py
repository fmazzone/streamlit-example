import streamlit as st
import pandas as pd
import numpy as np

st.title('Weather Forecasting Project')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    dataframe = pd.read_csv(uploaded_file)
    
    st.show(dataframe)
