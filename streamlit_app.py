import streamlit as st
import pandas as pd
import numpy as np
import datetime 

st.set_page_config(layout="centered", initial_sidebar_state="expanded")
st.title('_:blue[Weather Forecast]_')
st.image('https://www.analyticssteps.com/backend/media/thumbnail/6006173/6278986_1571298721_Weather_Forecoast_Graphics.jpg')

  
  # ------ layout setting---------------------------
window_selection_c = st.sidebar.container() # create an empty container in the sidebar
window_selection_c.markdown("## Insights") # add a title to the sidebar container
sub_columns = window_selection_c.columns(2) #Split the container into two columns for start and end date

# ----------Time window selection-----------------
YESTERDAY=datetime.date.today()-datetime.timedelta(days=1)
label="Giorno per la predizione"
st.date_input(label,datetime.date(2019, 7, 6))

