import streamlit as st
import pandas as pd
import numpy as np

st.title('Weather Forecasting Project')

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# Can be used wherever a "file-like" object is accepted:
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)
