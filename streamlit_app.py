import streamlit as st
import pandas as pd
import numpy as np
import datetime 

st.set_page_config(layout="centered", initial_sidebar_state="expanded")
st.title('_:blue[Weather Forecast]_')
st.image('https://www.analyticssteps.com/backend/media/thumbnail/6006173/6278986_1571298721_Weather_Forecoast_Graphics.jpg')

def nearest_day(DATE):
    """
    Takes a date and transform it to the nearest business day
    """
    if DATE.weekday() == 5:
        DATE = DATE - datetime.timedelta(days=1)

    if DATE.weekday() == 6:
        DATE = DATE + datetime.timedelta(days=1)
    return DATE
  
  # ------ layout setting---------------------------
window_selection_c = st.sidebar.container() # create an empty container in the sidebar
window_selection_c.markdown("## Insights") # add a title to the sidebar container
sub_columns = window_selection_c.columns(2) #Split the container into two columns for start and end date

# ----------Time window selection-----------------
YESTERDAY=datetime.date.today()-datetime.timedelta(days=1)
YESTERDAY = nearest_business_day(YESTERDAY) #Round to business day

DEFAULT_START=YESTERDAY - datetime.timedelta(days=700)
DEFAULT_START = nearest_day(DEFAULT_START)

START = sub_columns[0].date_input("From", value=DEFAULT_START, max_value=YESTERDAY - datetime.timedelta(days=1))

START = nearest_day(START)



