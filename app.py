import streamlit as st
import pandas as pd
from src.modules import charts as ch
from src.modules import metrics as mt


@st.cache
def load_data():
    data = pd.read_csv('TransformerMini-2022-01-24-120240.csv')
    data['Date'] = data[['Date', 'Time']].agg(' '.join, axis=1)
    data['Date'] = pd.to_datetime(data['Date'])
    data['GSpd(m/s)'] = data['GSpd(kmh)']/3.6
    data.drop(columns=['Time'], inplace=True)
    return data


st.set_page_config(page_title='Skyboy Quad Telemetry App', layout='wide')

st.title('Skyboy')
st.markdown('_A quadcopter telemetry log visualization app_')

# TODO: create a module to extract/calculate flight statistics & import

st.sidebar.title('Skyboy Utilities')
st.sidebar.markdown('_Data processing status:_')
data_load_state = st.sidebar.text('Loading data...')
flight_data = load_data()
data_load_state.text('Loading data and caching... done!')

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric('Date', mt.get_date(flight_data['Date']))
col2.metric('Time', mt.get_time(flight_data['Date']))
col3.metric('Flight Length', mt.get_flight_length(flight_data['Date']))
col4.metric('Capacity Used', mt.get_capacity_used(flight_data['Capa(mAh)']))
col5.metric('Transmitter Power', mt.get_tx_power(flight_data['TPWR(mW)']))

col1.metric('Max Distance from Home', '342 m')
col2.metric('Max Altitude', '55 m')
col3.metric('Max Ground Speed', '16.75 m/s')
col4.metric('Max Current Draw', '6 A')

if st.sidebar.checkbox('Show raw flight data'):
    st.subheader('Raw flight data')
    st.dataframe(flight_data)

chartcol1, chartcol2 = st.columns(2)

st.sidebar.markdown('_Charts:_')
if st.sidebar.checkbox('Flight dynamics', value=True):
    chartcol1.plotly_chart(ch.create_flight_dynamics_chart(flight_data))

if st.sidebar.checkbox('Battery stats', value=True):
    chartcol1.plotly_chart(ch.create_battery_chart(flight_data))

if st.sidebar.checkbox('Link quality', value=True):
    chartcol2.plotly_chart(ch.create_lq_chart(flight_data))

if st.sidebar.checkbox('Signal stats', value=True):
    chartcol2.plotly_chart(ch.create_signal_chart(flight_data))
