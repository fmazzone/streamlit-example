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
    data = pd.read_csv('https://drive.google.com/file/d/1-o3EvAMgSwzeB7p0EmIwmZM62Qh3akAn/view?usp=sharing', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date] = pd.to_datetime(data[date])
    return data

data_load_state = st.text('Loading data...')
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
