# Required Libraries
import streamlit as st
from matplotlib import dates
from datetime import datetime
from API import owm
from pyowm.commons.exceptions import NotFoundError

# Streamlit Display
st.set_page_config(layout="centered")
st.title(" 📅 WEATHER FORECASTER 🌥️ ☔ ")
