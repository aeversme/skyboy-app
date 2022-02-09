import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title='Skyboy Quad Telemetry App', layout='wide')

st.title('Skyboy')
st.markdown('_A quadcopter telemetry log visualization app_')
st.sidebar.title('Skyboy Utilities')
# TODO: create a section for flight statistics
# TODO: create a module to extract/calculate flight statistics & import


# load, transform, and cache CSV data
@st.cache
def load_data():
    data = pd.read_csv('TransformerMini-2022-01-24-120240.csv')
    data['Date'] = data[['Date', 'Time']].agg(' '.join, axis=1)
    data['Date'] = pd.to_datetime(data['Date'])
    data['GSpd(m/s)'] = data['GSpd(kmh)']/3.6
    data.drop(columns=['Time'], inplace=True)
    # data = data.pivot(columns='Date')
    return data


st.sidebar.write('Data processing status:')
data_load_state = st.sidebar.text('Loading data...')
flight_data = load_data()
data_load_state.text('Loading data and caching... done!')

show_data = st.sidebar.checkbox('Show raw flight data')
if show_data:
    # render raw data as a table
    st.subheader('Raw flight data')
    st.dataframe(flight_data)

st.sidebar.write('Charts:')
# TODO: add more charts (Batt/Pwr, Rx/Tx)
show_flight_dynamics = st.sidebar.checkbox('Flight dynamics')
if show_flight_dynamics:
    # render Flight Dynamics chart
    # TODO: break charts out into a separate module & import
    flight_dynamics = make_subplots(specs=[[{'secondary_y': True}]])
    flight_dynamics.add_trace(go.Scatter(x=flight_data['Date'], y=flight_data['Alt(m)'], name='Alt (m)', hoverinfo='y'),
                              secondary_y=False)
    flight_dynamics.add_trace(go.Scatter(x=flight_data['Date'], y=flight_data['GSpd(m/s)'], name='Ground Spd (m/s)',
                                         hoverinfo='y'),
                              secondary_y=True)
    flight_dynamics.add_trace(go.Scatter(x=flight_data['Date'], y=flight_data['VSpd(m/s)'], name='Vert Spd (m/s)',
                                         hoverinfo='y'), secondary_y=True)
    flight_dynamics.update_layout(title_text='Flight Dynamics')
    flight_dynamics.update_xaxes(title_text='Flight Time')
    flight_dynamics.update_yaxes(title_text='Altitude (m)', secondary_y=False)
    flight_dynamics.update_yaxes(title_text='Ground Speed (m/s)', secondary_y=True)
    st.plotly_chart(flight_dynamics, use_container_width=True)
