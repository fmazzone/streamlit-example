import streamlit as st
import pandas as pd
import time
#import joblib

st.set_page_config(
    page_title="Weather Forecast App",
    page_icon="🌡️", layout="wide",
    initial_sidebar_state="expanded"
)

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


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             #background-image: url("https://images.unsplash.com/photo-1541280910158-c4e14f9c94a3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80");
             #https://openweathermap.org/themes/openweathermap/assets/img/new-history-forecast-bulk.png
             #https://miro.medium.com/max/680/1*KYrYFzjUUlKSZlgFDzEEDg.png
             background-attachment: fixed;
             background-size: cover;
             background-color: #0E1117
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

title = '<p style="font-family:courier; color:#fcfcfc; font-size: 42px; font-style: italic">Weather Forecast</p>'
st.markdown(title, unsafe_allow_html=True)
#st.title(<*font color=‘red’>'_Weather Forecast_'</*font>, unsafe_allow_html=True)
subtitle = '<p style="font-family:courier; color:#fcfcfc; font-size: 20px; font-style: classic">Città considerate per la predizione</p>'
st.markdown(subtitle, unsafe_allow_html=True)
#st.subheader('Città considerate per la predizione')

df = pd.DataFrame({
    'Città': ['Milano', 'Torino', 'Firenze', 'Bologna', 'Roma', 'Napoli', 'Palermo'],
    'lat': [45.464664, 45.116177, 43.769562, 44.498955, 41.902782, 40.853294, 38.116669],
    'lon': [9.188540, 7.742615, 11.255814, 11.327591, 12.496366, 14.305573, 13.366667]
})

st.map(df)

# ------ layout setting---------------------------
window_selection_c = st.sidebar.container()  # create an empty container in the sidebar
dati = '<p style="font-family:courier; color:#fcfcfc; font-size: 20px; font-style: classic">Dati</p>'
window_selection_c.markdown(dati, unsafe_allow_html=True)  # add a title to the sidebar container
window_selection_c.text(
    "Compilare i campi" + "\n" + "e fare clic sul pulsante Predici." + "\n" + "Puoi scegliere se compilare" + "\n" + "tutti i campi o solo alcuni.")
sub_columns = window_selection_c.columns(1)

# informazioni base
città = sub_columns[0].selectbox('Seleziona città',
                                 ('Milano', 'Torino', 'Bologna', 'Firenze', 'Roma', 'Napoli', 'Palermo'))
temperatura = sub_columns[0].number_input('Seleziona temperatura °', -10, 50, 0)
vento = sub_columns[0].number_input('Seleziona velocità vento km/h', 0, 140, 0)
umidità = sub_columns[0].number_input('Seleziona umidità %', 0, 100, 0)

# informazioni avanzate
precipitazioni = sub_columns[0].number_input('Seleziona precipitazioni mm', 0.0, 2000.0, 0.0)
pressione = sub_columns[0].number_input('Seleziona pressione Pa', 0, 100, 0)
visibilità = sub_columns[0].number_input('Seleziona visibilità km', 0.0, 10.0, 0.0)
copertura = sub_columns[0].number_input('Seleziona copertura nuvolosa %', 0, 100, 0)

col1, col2, col3, col4, col5, col6, col7, = st.columns(7)  # divido la pagina in tante colonne quante sono le città

condMil = ''
condTor = ''
condFir = ''
condBol = ''
condRoma = ''
condNap = ''
condPal = ''

with col1:
    st.subheader("_MILANO_")
    st.image(
        "https://media.istockphoto.com/id/494084426/photo/milano-spirit.jpg?s=612x612&w=0&k=20&c=oRg0sCqikaBWGXSIgnvNVVu2cpHty9MF0spdieqpYoM=")
    #st.metric("Condizione", condMil)

with col2:
    st.subheader("_TORINO_")
    st.image(
        "https://media.istockphoto.com/id/940619078/photo/view-of-turin-city-centre-turin-italy.jpg?s=612x612&w=0&k=20&c=3vs4AeYD5yAQuig7P6lD02wsRBaKAQPXi_wGVdQQxro=")
    #st.metric("Condizione", condTor)

with col3:
    st.subheader("_FIRENZE_")
    st.image(
        "https://media.istockphoto.com/id/483876975/photo/panorama-of-florence-and-saint-mary.jpg?s=612x612&w=0&k=20&c=tK2fS2Vaoq6-r0kD1NOfz8IrgXCrP3bVjfTBUZv7z5I=")
    #st.metric("Condizione", condFir)

with col4:
    st.subheader("_BOLOGNA_")
    st.image("https://static2-viaggi.corriereobjects.it/wp-content/uploads/2020/01/bologna.jpg?v=415423")
    #st.metric("Condizione", condBol)

with col5:
    st.subheader("_ROMA_")
    st.image(
        "https://media.istockphoto.com/id/539115110/photo/colosseum-in-rome-and-morning-sun-italy.jpg?s=612x612&w=0&k=20&c=9NtFxHI3P2IBWRY9t0NrfPZPR4iusHmVLbXg2Cjv9Fs=")
    #st.metric("Condizione", condRoma)

with col6:
    st.subheader("_NAPOLI_")
    st.image(
        "https://media.istockphoto.com/id/1327485657/photo/naples-at-sunset-gulf-of-naples-italy.jpg?b=1&s=170667a&w=0&k=20&c=Bji5m-48zMeGQ8mwo4a9wof3rQnSJzaIYpU5OlnGVIs=")
    #st.metric("Condizione", condNap)

with col7:
    st.subheader("_PALERMO_")
    st.image("https://www.filoteapasta.com/wp-content/uploads/2019/07/Cattedrale-Palermo.jpg")
    #st.metric("Condizione", condPal)


##________Pred
### Aggiungere controllo della città per cui fare la predizione

@st.cache(allow_output_mutation=True)
def load(model_path, scaler_path, encoder_path):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    encoder = joblib.load(encoder_path)
    return model, scaler, encoder


def inference(row, model, scaler, encoder, feat_cols):
    df = pd.DataFrame([row], columns=feat_cols)
    X = scaler.transform(df)
    features = pd.DataFrame(X, columns=feat_cols)
    prediction = model.predict(features)
    prediction = encoder.inverse_transform(prediction)
    return prediction


row = [temperatura, vento, umidità, precipitazioni, pressione, visibilità, copertura]

if st.button('_Predici_'):
    with st.spinner('Attendere...'):
        time.sleep(5)

        feat_cols = ['tempC', 'windspeedKmph', 'precipMM', 'humidity', 'visibility', 'pressure', 'cloudcover']

        # location --> variabile --> la città che ha scelto

        location = 'milan'

        ##sc, model = load('models/scaler.joblib', 'models/model.joblib')
        model, scaler, encoder = load(f'models/{location}_random_forest_gini.joblib',
                                      f'models/{location}_scaler.joblib', f'models/{location}_encoder.joblib')
        result = inference(row, model, scaler, encoder, feat_cols)
        #st.write(result)
        if 'Sunny' in str(result):
            result = 'Sunny'
        col1.metric("Condizione prevista: ", result)
