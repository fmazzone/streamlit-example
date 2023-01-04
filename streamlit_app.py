import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import time 


st.set_page_config(page_title="Weather Forecast App",page_icon="🌡️",layout="wide", initial_sidebar_state="expanded")
st.title('_Weather Forecast_')

df = pd.DataFrame({
   'Città':['Milano', 'Torino', 'Firenze', 'Bologna', 'Roma', 'Napoli', 'Palermo'],
    'lat':[45.464664, 45.116177,  43.769562, 44.498955, 41.902782, 40.853294, 38.116669],
    'lon':[9.188540, 7.742615, 11.255814, 11.327591, 12.496366, 14.305573, 13.366667]
})

st.map(df)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/510656547/video/soft-moving-cloud-for-weather-report-background.jpg?s=640x640&k=20&c=xBW8VeBDgE5IPpwrprN45GOe7HYU_Q1Rh7Q7WZdjIZo=");
             #https://openweathermap.org/themes/openweathermap/assets/img/new-history-forecast-bulk.png
             #https://miro.medium.com/max/680/1*KYrYFzjUUlKSZlgFDzEEDg.png
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


  # ------ layout setting---------------------------
window_selection_c = st.sidebar.container() # create an empty container in the sidebar
window_selection_c.markdown("## _Dati_") # add a title to the sidebar container
sub_columns = window_selection_c.columns(2) #Split the container into two columns 

sub_columns[0].subheader('Informazioni')

sub_columns[0].text_input('Temperatura')
sub_columns[0].text_input('vento')
sub_columns[0].text_input('umidità')

sub_columns[0].subheader('Avanzate')

sub_columns[0].text_input('Temperatura')
sub_columns[0].text_input('vento')
sub_columns[0].text_input('umidità')

   
sub_columns[0].button('Inserisci')

col1, col2, col3,col4,col5,col6,col7, = st.columns(7)

with col1:
   st.subheader("_MILANO_")
   st.image("https://media.istockphoto.com/id/494084426/photo/milano-spirit.jpg?s=612x612&w=0&k=20&c=oRg0sCqikaBWGXSIgnvNVVu2cpHty9MF0spdieqpYoM=")
   st.metric("Condizione", "stringa")
   with st.expander("Dati real time"):
     st.metric("Temperatura", "°")
     st.metric("Vento", "km/h")
     st.metric("Umidità", "%")
    
with col2:
   st.subheader("_TORINO_")
   st.image("https://media.istockphoto.com/id/940619078/photo/view-of-turin-city-centre-turin-italy.jpg?s=612x612&w=0&k=20&c=3vs4AeYD5yAQuig7P6lD02wsRBaKAQPXi_wGVdQQxro=")
   st.metric("Condizione", "stringa")
   with st.expander("Dati real time"):
     st.metric("Temperatura", "-")
     st.metric("Vento", "-")
     st.metric("Umidità", "-")
    
with col3:
   st.subheader("_FIRENZE_")
   st.image("data:image/jpeg;base64,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")
   st.metric("Condizione", "stringa")
   with st.expander("Dati real time"):
     st.metric("Temperatura", "-")
     st.metric("Vento", "-")
     st.metric("Umidità", "-")
  
with col4:
   st.subheader("_BOLOGNA_")
   st.image("https://static2-viaggi.corriereobjects.it/wp-content/uploads/2020/01/bologna.jpg?v=415423")
   st.metric("Condizione", "stringa")
   with st.expander("Dati real time"):
     st.metric("Temperatura", "-")
     st.metric("Vento", "-")
     st.metric("Umidità", "-")
    
with col5:
   st.subheader("_ROMA_")
   st.image("data:image/jpeg;base64,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")
   st.metric("Condizione", "stringa")
   with st.expander("Dati real time"):
     st.metric("Temperatura", "-")
     st.metric("Vento", "-")
     st.metric("Umidità", "-")
  
with col6:
   st.subheader("_NAPOLI_")
   st.image("https://media.istockphoto.com/id/1327485657/photo/naples-at-sunset-gulf-of-naples-italy.jpg?b=1&s=170667a&w=0&k=20&c=Bji5m-48zMeGQ8mwo4a9wof3rQnSJzaIYpU5OlnGVIs=")
   st.metric("Condizione", "stringa")
   with st.expander("Dati real time"):
     st.metric("Temperatura", "-")
     st.metric("Vento", "-")
     st.metric("Umidità", "-") 
    
with col7:
   st.subheader("_PALERMO_")
   st.image("https://www.filoteapasta.com/wp-content/uploads/2019/07/Cattedrale-Palermo.jpg")
   st.metric("Condizione", "stringa")
   with st.expander("Dati real time"):
     st.metric("Temperatura", "-")
     st.metric("Vento", "-")
     st.metric("Umidità", "-")

#st.markdown("""
#<style>
#div.stButton > button:first-child {
#    background-color: rgb(234,230,202);
#    text-color:rgb(10,230,202);
#}
#</style>""", unsafe_allow_html=True)    
 
st.markdown(""" 
<style>
div.stButton > button:first-child {
background-color: #4682B4;color:WhiteSmoke;font-size:20px;height:3em;width:10em;border-radius:10px 10px 10px 10px;
}
.css-2trqyj:focus:not(:active) {
border-color: #ffffff;
box-shadow: none;
color: #ffffff;
background-color: #3f5973;
}
.css-2trqyj:focus:(:active) {
border-color: #ffffff;
box-shadow: none;
color: #ffffff;
background-color: #3f5973;
}
.css-2trqyj:focus:active){
background-color: #3f5973;
border-color: #ffffff;
box-shadow: none;
color: #ffffff;
background-color: #0066cc;
}
</style>""", unsafe_allow_html=True)    
    
if st.button('_Predici_'):
    with st.spinner('Attendere...'):
      time.sleep(5)
    

 
