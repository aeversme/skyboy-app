import streamlit as st
import pandas as pd
from src.modules import data_conversion as dc
from src.modules import charts as ch
from src.modules import metrics as mt


@st.cache
def load_data():
    data = pd.read_csv('TransformerMini-2022-01-24-114643.csv')
    converted_data = dc.convert_df(data)
    return converted_data


st.set_page_config(page_title='Skyboy Quad Telemetry App', layout='wide')

st.title('Skyboy')
st.markdown('_A quadcopter telemetry log visualization app_')

st.sidebar.title('Skyboy Utilities')
st.sidebar.markdown('_Data processing status:_')
data_load_state = st.sidebar.text('Loading data...')
flight_data = load_data()
data_load_state.text('Loading data and caching... done!')

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric('Date', mt.get_date(flight_data['Date']))
col2.metric('Time', mt.get_time(flight_data['Date']))
col3.metric('Flight Length', mt.get_flight_length(flight_data['Date']))
col4.metric('Flight Distance', mt.calc_flight_distance(flight_data['GPS']))
col5.metric('Max Distance from Home', mt.calc_max_distance(flight_data['GPS']))

col1.metric('Max Altitude', mt.get_max_altitude(flight_data['Alt(m)']))
col2.metric('Max Ground Speed', mt.get_max_ground_speed(flight_data['GSpd(m/s)']))
col3.metric('Max Current Draw', mt.get_max_current(flight_data['Curr(A)']))
col4.metric('Capacity Used', mt.get_capacity_used(flight_data['Capa(mAh)']))
col5.metric('Transmitter Power', mt.get_tx_power(flight_data['TPWR(mW)']))

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
