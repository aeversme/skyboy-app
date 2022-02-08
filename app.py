import streamlit as st
import pandas as pd

st.title('Skyboy')


# load and cache CSV data
@st.cache
def load_data():
    data = pd.read_csv('TransformerMini-2022-01-24-120240.csv')
    return data


data_load_state = st.text('Loading data...')
flight_data = load_data()
data_load_state.text('Loading data and caching... done!')

# render raw data as a table
st.subheader('Raw flight data')
st.write(flight_data)
