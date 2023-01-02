# Required Libraries
import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

# Streamlit Display
st.set_page_config(layout="centered")
st.title(" 📅 WEATHER FORECASTER 🌥️ ☔ ")

DATE_COLUMN = 'date/time'

@st.cache
def load_data(nrows):
    data = pd.read_csv('https://drive.google.com/file/d/1-o3EvAMgSwzeB7p0EmIwmZM62Qh3akAn/view?usp=sharing',nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date] = pd.to_datetime(data[date])
    return data

data_load_state = st.text('Loading data...')
data = load_data(6670)
data_load_state.text("Done! (using st.cache)")
st.table(data)


