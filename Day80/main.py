import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import plotly.express as px
st.title('Comparison chart')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
data_path = "F:/Projekte/DataScience Jupyter Notebooks"


def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

@st.cache
def load_data(nrows):
    data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

files = os.listdir(data_path)
files = [file for file in files if file.endswith(".csv")]

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    (files)
)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
st.text(add_selectbox)
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta

fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
st.pyplot(fig)

col1, col2 = st.columns(2)


fig2 = px.scatter_polar(r=range(45, 90, 5), theta=range(0, 45, 5),
                       range_theta=[0,90], start_angle=90)
col1.plotly_chart(fig2)
col1.write("Fig2")
fig3 = px.scatter_polar(r=range(0, 90, 10), theta=range(90, 180, 10),
                        range_theta=[0,90], start_angle=180, direction='clockwise')
col2.plotly_chart(fig3, use_container_width=False)
col2.write("Fig3")
fig4 = px.scatter_polar(r=range(0, 90, 10), theta=range(180, 270, 10),
                        range_theta=[90, 180], start_angle=270, direction='counterclockwise')
col1.plotly_chart(fig4, use_container_width=False)
col1.write("Fig4")
fig5 = px.scatter_polar(r=range(0, 90, 10), theta=range(270, 360, 10),
                        range_theta=[180, 270], start_angle=270, direction='counterclockwise')
col2.plotly_chart(fig5, use_container_width=False)
col2.write("Fig5")
az = [10 for i in range(0,100)]
range_n = [i for i in range(0,100)]
st.write("PSR")
fig6 = px.scatter_polar(r=range_n, theta=az,
                        range_theta=[0,90], start_angle=0, direction='counterclockwise')
st.plotly_chart(fig6, use_container_width=False)
