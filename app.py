import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
from datetime import timedelta
import plotly.graph_objects as go
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, plot_components_plotly
import warnings
import streamlit.components.v1 as components
import time
import plotly.figure_factory as ff

warnings.filterwarnings('ignore')
pd.options.display.float_format = '${:,.2f}'.format
today = datetime.today().strftime('%Y-%m-%d')
start_date = '2016-01-01'
currency = st.radio("Which Currency do you want to predict",('ETH-USD', 'Drama', 'Documentary'))
eth_df = yf.download(currency,start_date, today)
st.write(eth_df.head())
