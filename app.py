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
from PIL import Image

warnings.filterwarnings('ignore')
pd.options.display.float_format = '${:,.2f}'.format
today = datetime.today().strftime('%Y-%m-%d')
start_date = '2016-01-01'

rad=st.sidebar.radio("Menu",["Homepage","History of currency","History of currency with Candlesticks","Currency Price Prediction","Custom","About Us"])
if rad=='Homepage':
  
  image = Image.open("wp3624608.webp")
  
  st.image(image, caption='Crypto Currency Prediction')
  st.snow()
elif rad == "History of currency":
  currency = st.selectbox("Which Currency do you want to predict",('ADA-USD', 'AERGO-USD', 'AGLD-USD', 'ALGO-USD', 'ALI2-USD', 'ALICE-USD', 'ALPACA-USD', 'ALPINE-USD', 'AMP-USD', 'AMPL-USD', 'ANY-USD', 'AQT-USD', 'AR-USD', 'ARDR-USD', 'ARPA-USD', 'ATA-USD', 'ATOM-USD', 'AURORA1-USD', 'AVAX-USD', 'BAT-USD', 'BCD-USD', 'BCH-USD', 'BEST-USD', 'BIOT-USD', 'BNANA-USD', 'BNB-USD', 'BNX-USD', 'BOBA-USD', 'BOR-USD', 'BOSON-USD', 'BRG-USD', 'BSW-USD', 'BTC-USD', 'BTCB-USD', 'BTCST-USD', 'BTS-USD', 'BUSD-USD', 'BZRX-USD', 'BZZ-USD', 'C98-USD', 'CBK-USD', 'CELO-USD', 'CHR-USD', 'CHZ-USD', 'CLV-USD', 'COMP1-USD', 'CON-USD', 'CORE-USD', 'COTI-USD', 'COVAL-USD', 'CQT-USD', 'CRE-USD', 'CRO-USD', 'CRV-USD', 'CTK-USD', 'CTSI-USD', 'CUBE-USD', 'CUDOS-USD', 'CUSD-USD', 'CVX-USD', 'CVX-USD', 'DAD-USD', 'DAG-USD', 'DAI-USD', 'DAO-USD', 'DAR-USD', 'DASH-USD', 'DCR-USD', 'DENT-USD', 'DIVI-USD', 'DNT-USD', 'DOGE-USD', 'DOT-USD', 'DPR-USD', 'DSV-USD', 'EFI-USD', 'EGG-USD', 'ELF-USD', 'ENJ-USD', 'ENS-USD', 'EPS1-USD', 'ERN-USD', 'ETC-USD', 'ETH-USD', 'EUM-USD', 'FARM-USD', 'FET-USD', 'FIDA-USD', 'FIL-USD', 'FLM-USD', 'FORTH-USD', 'FRTS-USD', 'FTT-USD', 'FX-USD', 'GALA-USD', 'GMT1-USD', 'GMT3-USD', 'GTC2-USD', 'GUSD-USD', 'HBTC-USD', 'HERO1-USD', 'HEX-USD', 'HI-USD', 'HNS-USD', 'HT-USD', 'HUM-USD', 'HUNT-USD', 'HYDRA-USD', 'ICP-USD', 'INJ-USD', 'IRIS-USD', 'JASMY-USD', 'JILL-USD', 'JOE-USD', 'KDA-USD', 'KMD-USD', 'KP3R-USD', 'KSN-USD', 'LDO-USD', 'LEO-USD', 'LINK-USD', 'LOKA-USD', 'LOOM-USD', 'LRC-USD', 'LSK-USD', 'LTC-USD', 'LTO-USD', 'LUNA1-USD', 'LYXE-USD', 'MANA-USD', 'MATIC-USD', 'MBOX-USD', 'MC-USD', 'MDX1-USD', 'MED-USD', 'METIS-USD', 'MFT-USD', 'MINA-USD', 'MLK-USD', 'MNW-USD', 'MOB-USD', 'MOC-USD', 'MOVR-USD', 'MPL-USD', 'MTL-USD', 'MVIXY-USD', 'MVL-USD', 'MX-USD', 'MXC-USD', 'NEAR-USD', 'NEO-USD', 'NEXO-USD', 'NOIA-USD', 'NU-USD', 'OGN-USD', 'OKB-USD', 'ONE1-USD', 'ONG1-USD', 'ONUS-USD', 'ORBS-USD', 'ORC-USD', 'OSMO-USD', 'PCL-USD', 'PEAK-USD', 'PEOPLE-USD', 'PERP-USD', 'PHA-USD', 'PLTC-USD', 'POWR-USD', 'PRE-USD', 'PUNDIX-USD', 'PYR-USD', 'QC-USD', 'QNT-USD', 'QUICK-USD', 'RAY-USD', 'REQ-USD', 'RFR-USD', 'RGT-USD', 'RISE1-USD', 'ROOK-USD', 'RSR-USD', 'SDAO-USD', 'SE SFP-USD', 'SHIB-USD', 'SLP-USD', 'SNT-USD', 'SOL-USD', 'SOUL-USD', 'SOV-USD', 'SPS-USD', 'STETH-USD', 'STMX-USD', 'SUPER1-USD', 'SURE-USD', 'TAVA-USD', 'TITAN-USD', 'TKO-USD', 'TLM-USD', 'TLOS-USD', 'TRAC-USD', 'TRIBE-USD', 'TROY-USD', 'TRX-USD', 'TUSD-USD', 'TVK-USD', 'UFO2-USD', 'UNI1-USD', 'UOS-USD', 'UPP-USD', 'UQC-USD', 'USDC-USD', 'USDN-USD', 'USDP-USD', 'USDT-USD', 'USDX2-USD', 'UST-USD', 'VELO-USD', 'VERI-USD', 'VET-USD', 'VRA-USD', 'VRSC-USD', 'VTHO-USD', 'VXV-USD', 'WAN-USD', 'WBTC-USD', 'WIN-USD', 'WNCG-USD', 'WOZX-USDLINA1-USD', 'WRFOX-USD', 'WRX-USD', 'WTRX-USD', 'WWXT-USD', 'XAUT-USD', 'XCAD-USD', 'XCH-USD', 'XHV-USD', 'XLCX-USD', 'XLM-USD', 'XMR-USD', 'XNO-USD', 'XPRT-USD', 'XRP-USD', 'XVG-USD', 'XYO-USD', 'YFII-USD', 'YGG-USD', 'ZB-USD'))
  eth_df = yf.download(currency,start_date, today)
  eth_df.reset_index(inplace=True)
  # eth_df.columns

  df = eth_df[["Date", "Open"]]

  new_names = {
      "Date": "ds", 
      "Open": "y",
  }

  df.rename(columns=new_names, inplace=True)

  # df.tail()

  # plot the open price

  x = df["ds"]
  y = df["y"]
  # st.area_chart(y)
  fig = go.Figure()

  bb=fig.add_trace(go.Scatter(x=x, y=y))
  # st.write("# History of Ethereum")

  # Set title
  fig.update_layout(
      title_text="Time series plot of currency open price",
  )
  fig2 = go.Figure(data=[go.Candlestick(x=eth_df['Date'],
                  open=eth_df['Open'],
                  high=eth_df['High'],
                  low=eth_df['Low'],
                  close=eth_df['Close'])])
  # st.write("# History of Ethereum with Candlesticks")

  fig2.update_layout(
      xaxis=dict(
          rangeselector=dict(
              buttons=list(
                  [
                      dict(count=1, label="1m", step="month", stepmode="backward"),
                      dict(count=6, label="6m", step="month", stepmode="backward"),
                      dict(count=1, label="YTD", step="year", stepmode="todate"),
                      dict(count=1, label="1y", step="year", stepmode="backward"),
                      dict(step="all"),
                  ]
              )
          ),
          rangeslider=dict(visible=True),
          type="date",
      )
  )

  fig.update_layout(
      xaxis=dict(
          rangeselector=dict(
              buttons=list(
                  [
                      dict(count=1, label="1m", step="month", stepmode="backward"),
                      dict(count=6, label="6m", step="month", stepmode="backward"),
                      dict(count=1, label="YTD", step="year", stepmode="todate"),
                      dict(count=1, label="1y", step="year", stepmode="backward"),
                      dict(step="all"),
                  ]
              )
          ),
          rangeslider=dict(visible=True),
          type="date",
      )
  )

  m = Prophet(
      seasonality_mode="multiplicative" 
  )

  m.fit(df)

  future = m.make_future_dataframe(periods = 365)
  future.tail()

  forecast = m.predict(future)
  forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

  next_day = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')


  aa=plot_plotly(m, forecast)
  #st.write("# Ethereum Coin Price Prediction")
  # st.write(aa)



  plot_components_plotly(m, forecast)
  progress = st.progress(0)
  for i in range(0,2):
    time.sleep(0.2)
    progress.progress((i+1)*100-100)
  st.write("# History of currency")
  st.write(bb)
  #
  # col1 = st.columns(1)
  from datetime import date
  today = date.today()
  # d1 = today.strftime("%Y-%m-%d")
  # yesterday = today - timedelta(days = 1)
  # d2 = yesterday.strftime("%Y-%m-%d")
  # for i in forecast.index:
  #     if(today == forecast['ds'][i]):
  #       col1.metric("Change", forecast['yhat'][i], forecast['yhat'][i]-forecast['yhat'][i-1])
  col1= st.columns(1)
  for i in forecast.index:
    if(today == forecast['ds'][i]):
      r1=forecast['yhat'][i]
      r2=r1/100
  
      st.write(r1," Dollars")
  #r1=int(r1)
  #r2=int(r2)
  #col1.metric("ETH",r1,r2)
  #st.write(forecast)


elif rad == "History of currency with Candlesticks":
  currency = st.selectbox("Which Currency do you want to predict",('ADA-USD', 'AERGO-USD', 'AGLD-USD', 'ALGO-USD', 'ALI2-USD', 'ALICE-USD', 'ALPACA-USD', 'ALPINE-USD', 'AMP-USD', 'AMPL-USD', 'ANY-USD', 'AQT-USD', 'AR-USD', 'ARDR-USD', 'ARPA-USD', 'ATA-USD', 'ATOM-USD', 'AURORA1-USD', 'AVAX-USD', 'BAT-USD', 'BCD-USD', 'BCH-USD', 'BEST-USD', 'BIOT-USD', 'BNANA-USD', 'BNB-USD', 'BNX-USD', 'BOBA-USD', 'BOR-USD', 'BOSON-USD', 'BRG-USD', 'BSW-USD', 'BTC-USD', 'BTCB-USD', 'BTCST-USD', 'BTS-USD', 'BUSD-USD', 'BZRX-USD', 'BZZ-USD', 'C98-USD', 'CBK-USD', 'CELO-USD', 'CHR-USD', 'CHZ-USD', 'CLV-USD', 'COMP1-USD', 'CON-USD', 'CORE-USD', 'COTI-USD', 'COVAL-USD', 'CQT-USD', 'CRE-USD', 'CRO-USD', 'CRV-USD', 'CTK-USD', 'CTSI-USD', 'CUBE-USD', 'CUDOS-USD', 'CUSD-USD', 'CVX-USD', 'CVX-USD', 'DAD-USD', 'DAG-USD', 'DAI-USD', 'DAO-USD', 'DAR-USD', 'DASH-USD', 'DCR-USD', 'DENT-USD', 'DIVI-USD', 'DNT-USD', 'DOGE-USD', 'DOT-USD', 'DPR-USD', 'DSV-USD', 'EFI-USD', 'EGG-USD', 'ELF-USD', 'ENJ-USD', 'ENS-USD', 'EPS1-USD', 'ERN-USD', 'ETC-USD', 'ETH-USD', 'EUM-USD', 'FARM-USD', 'FET-USD', 'FIDA-USD', 'FIL-USD', 'FLM-USD', 'FORTH-USD', 'FRTS-USD', 'FTT-USD', 'FX-USD', 'GALA-USD', 'GMT1-USD', 'GMT3-USD', 'GTC2-USD', 'GUSD-USD', 'HBTC-USD', 'HERO1-USD', 'HEX-USD', 'HI-USD', 'HNS-USD', 'HT-USD', 'HUM-USD', 'HUNT-USD', 'HYDRA-USD', 'ICP-USD', 'INJ-USD', 'IRIS-USD', 'JASMY-USD', 'JILL-USD', 'JOE-USD', 'KDA-USD', 'KMD-USD', 'KP3R-USD', 'KSN-USD', 'LDO-USD', 'LEO-USD', 'LINK-USD', 'LOKA-USD', 'LOOM-USD', 'LRC-USD', 'LSK-USD', 'LTC-USD', 'LTO-USD', 'LUNA1-USD', 'LYXE-USD', 'MANA-USD', 'MATIC-USD', 'MBOX-USD', 'MC-USD', 'MDX1-USD', 'MED-USD', 'METIS-USD', 'MFT-USD', 'MINA-USD', 'MLK-USD', 'MNW-USD', 'MOB-USD', 'MOC-USD', 'MOVR-USD', 'MPL-USD', 'MTL-USD', 'MVIXY-USD', 'MVL-USD', 'MX-USD', 'MXC-USD', 'NEAR-USD', 'NEO-USD', 'NEXO-USD', 'NOIA-USD', 'NU-USD', 'OGN-USD', 'OKB-USD', 'ONE1-USD', 'ONG1-USD', 'ONUS-USD', 'ORBS-USD', 'ORC-USD', 'OSMO-USD', 'PCL-USD', 'PEAK-USD', 'PEOPLE-USD', 'PERP-USD', 'PHA-USD', 'PLTC-USD', 'POWR-USD', 'PRE-USD', 'PUNDIX-USD', 'PYR-USD', 'QC-USD', 'QNT-USD', 'QUICK-USD', 'RAY-USD', 'REQ-USD', 'RFR-USD', 'RGT-USD', 'RISE1-USD', 'ROOK-USD', 'RSR-USD', 'SDAO-USD', 'SE SFP-USD', 'SHIB-USD', 'SLP-USD', 'SNT-USD', 'SOL-USD', 'SOUL-USD', 'SOV-USD', 'SPS-USD', 'STETH-USD', 'STMX-USD', 'SUPER1-USD', 'SURE-USD', 'TAVA-USD', 'TITAN-USD', 'TKO-USD', 'TLM-USD', 'TLOS-USD', 'TRAC-USD', 'TRIBE-USD', 'TROY-USD', 'TRX-USD', 'TUSD-USD', 'TVK-USD', 'UFO2-USD', 'UNI1-USD', 'UOS-USD', 'UPP-USD', 'UQC-USD', 'USDC-USD', 'USDN-USD', 'USDP-USD', 'USDT-USD', 'USDX2-USD', 'UST-USD', 'VELO-USD', 'VERI-USD', 'VET-USD', 'VRA-USD', 'VRSC-USD', 'VTHO-USD', 'VXV-USD', 'WAN-USD', 'WBTC-USD', 'WIN-USD', 'WNCG-USD', 'WOZX-USDLINA1-USD', 'WRFOX-USD', 'WRX-USD', 'WTRX-USD', 'WWXT-USD', 'XAUT-USD', 'XCAD-USD', 'XCH-USD', 'XHV-USD', 'XLCX-USD', 'XLM-USD', 'XMR-USD', 'XNO-USD', 'XPRT-USD', 'XRP-USD', 'XVG-USD', 'XYO-USD', 'YFII-USD', 'YGG-USD', 'ZB-USD'))
  eth_df = yf.download(currency,start_date, today)

  eth_df.reset_index(inplace=True)
  # eth_df.columns

  df = eth_df[["Date", "Open"]]

  new_names = {
      "Date": "ds", 
      "Open": "y",
  }

  df.rename(columns=new_names, inplace=True)

  # df.tail()

  # plot the open price

  x = df["ds"]
  y = df["y"]
  # st.area_chart(y)
  fig = go.Figure()

  bb=fig.add_trace(go.Scatter(x=x, y=y))
  # st.write("# History of Ethereum")

  # Set title
  fig.update_layout(
      title_text="Time series plot of currency Open Price",
  )
  fig2 = go.Figure(data=[go.Candlestick(x=eth_df['Date'],
                  open=eth_df['Open'],
                  high=eth_df['High'],
                  low=eth_df['Low'],
                  close=eth_df['Close'])])
  # st.write("# History of Ethereum with Candlesticks")

  fig2.update_layout(
      xaxis=dict(
          rangeselector=dict(
              buttons=list(
                  [
                      dict(count=1, label="1m", step="month", stepmode="backward"),
                      dict(count=6, label="6m", step="month", stepmode="backward"),
                      dict(count=1, label="YTD", step="year", stepmode="todate"),
                      dict(count=1, label="1y", step="year", stepmode="backward"),
                      dict(step="all"),
                  ]
              )
          ),
          rangeslider=dict(visible=True),
          type="date",
      )
  )

  fig.update_layout(
      xaxis=dict(
          rangeselector=dict(
              buttons=list(
                  [
                      dict(count=1, label="1m", step="month", stepmode="backward"),
                      dict(count=6, label="6m", step="month", stepmode="backward"),
                      dict(count=1, label="YTD", step="year", stepmode="todate"),
                      dict(count=1, label="1y", step="year", stepmode="backward"),
                      dict(step="all"),
                  ]
              )
          ),
          rangeslider=dict(visible=True),
          type="date",
      )
  )

  m = Prophet(
      seasonality_mode="multiplicative" 
  )

  m.fit(df)

  future = m.make_future_dataframe(periods = 365)
  future.tail()

  forecast = m.predict(future)
  forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

  next_day = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')


  aa=plot_plotly(m, forecast)
  #st.write("# Ethereum Coin Price Prediction")
  # st.write(aa)



  plot_components_plotly(m, forecast)

  progress = st.progress(0)
  for i in range(0,2):
    time.sleep(0.2)
    progress.progress((i+1)*100-100)
  st.write("# History of currency with Candlesticks")
  st.write(fig2)
elif rad == "Currency Price Prediction":
  progress = st.progress(0)
  for i in range(0,2):
    time.sleep(0.2)
    progress.progress((i+1)*100-100)
  currency = st.selectbox("Which Currency do you want to predict",('ADA-USD', 'AERGO-USD', 'AGLD-USD', 'ALGO-USD', 'ALI2-USD', 'ALICE-USD', 'ALPACA-USD', 'ALPINE-USD', 'AMP-USD', 'AMPL-USD', 'ANY-USD', 'AQT-USD', 'AR-USD', 'ARDR-USD', 'ARPA-USD', 'ATA-USD', 'ATOM-USD', 'AURORA1-USD', 'AVAX-USD', 'BAT-USD', 'BCD-USD', 'BCH-USD', 'BEST-USD', 'BIOT-USD', 'BNANA-USD', 'BNB-USD', 'BNX-USD', 'BOBA-USD', 'BOR-USD', 'BOSON-USD', 'BRG-USD', 'BSW-USD', 'BTC-USD', 'BTCB-USD', 'BTCST-USD', 'BTS-USD', 'BUSD-USD', 'BZRX-USD', 'BZZ-USD', 'C98-USD', 'CBK-USD', 'CELO-USD', 'CHR-USD', 'CHZ-USD', 'CLV-USD', 'COMP1-USD', 'CON-USD', 'CORE-USD', 'COTI-USD', 'COVAL-USD', 'CQT-USD', 'CRE-USD', 'CRO-USD', 'CRV-USD', 'CTK-USD', 'CTSI-USD', 'CUBE-USD', 'CUDOS-USD', 'CUSD-USD', 'CVX-USD', 'CVX-USD', 'DAD-USD', 'DAG-USD', 'DAI-USD', 'DAO-USD', 'DAR-USD', 'DASH-USD', 'DCR-USD', 'DENT-USD', 'DIVI-USD', 'DNT-USD', 'DOGE-USD', 'DOT-USD', 'DPR-USD', 'DSV-USD', 'EFI-USD', 'EGG-USD', 'ELF-USD', 'ENJ-USD', 'ENS-USD', 'EPS1-USD', 'ERN-USD', 'ETC-USD', 'ETH-USD', 'EUM-USD', 'FARM-USD', 'FET-USD', 'FIDA-USD', 'FIL-USD', 'FLM-USD', 'FORTH-USD', 'FRTS-USD', 'FTT-USD', 'FX-USD', 'GALA-USD', 'GMT1-USD', 'GMT3-USD', 'GTC2-USD', 'GUSD-USD', 'HBTC-USD', 'HERO1-USD', 'HEX-USD', 'HI-USD', 'HNS-USD', 'HT-USD', 'HUM-USD', 'HUNT-USD', 'HYDRA-USD', 'ICP-USD', 'INJ-USD', 'IRIS-USD', 'JASMY-USD', 'JILL-USD', 'JOE-USD', 'KDA-USD', 'KMD-USD', 'KP3R-USD', 'KSN-USD', 'LDO-USD', 'LEO-USD', 'LINK-USD', 'LOKA-USD', 'LOOM-USD', 'LRC-USD', 'LSK-USD', 'LTC-USD', 'LTO-USD', 'LUNA1-USD', 'LYXE-USD', 'MANA-USD', 'MATIC-USD', 'MBOX-USD', 'MC-USD', 'MDX1-USD', 'MED-USD', 'METIS-USD', 'MFT-USD', 'MINA-USD', 'MLK-USD', 'MNW-USD', 'MOB-USD', 'MOC-USD', 'MOVR-USD', 'MPL-USD', 'MTL-USD', 'MVIXY-USD', 'MVL-USD', 'MX-USD', 'MXC-USD', 'NEAR-USD', 'NEO-USD', 'NEXO-USD', 'NOIA-USD', 'NU-USD', 'OGN-USD', 'OKB-USD', 'ONE1-USD', 'ONG1-USD', 'ONUS-USD', 'ORBS-USD', 'ORC-USD', 'OSMO-USD', 'PCL-USD', 'PEAK-USD', 'PEOPLE-USD', 'PERP-USD', 'PHA-USD', 'PLTC-USD', 'POWR-USD', 'PRE-USD', 'PUNDIX-USD', 'PYR-USD', 'QC-USD', 'QNT-USD', 'QUICK-USD', 'RAY-USD', 'REQ-USD', 'RFR-USD', 'RGT-USD', 'RISE1-USD', 'ROOK-USD', 'RSR-USD', 'SDAO-USD', 'SE SFP-USD', 'SHIB-USD', 'SLP-USD', 'SNT-USD', 'SOL-USD', 'SOUL-USD', 'SOV-USD', 'SPS-USD', 'STETH-USD', 'STMX-USD', 'SUPER1-USD', 'SURE-USD', 'TAVA-USD', 'TITAN-USD', 'TKO-USD', 'TLM-USD', 'TLOS-USD', 'TRAC-USD', 'TRIBE-USD', 'TROY-USD', 'TRX-USD', 'TUSD-USD', 'TVK-USD', 'UFO2-USD', 'UNI1-USD', 'UOS-USD', 'UPP-USD', 'UQC-USD', 'USDC-USD', 'USDN-USD', 'USDP-USD', 'USDT-USD', 'USDX2-USD', 'UST-USD', 'VELO-USD', 'VERI-USD', 'VET-USD', 'VRA-USD', 'VRSC-USD', 'VTHO-USD', 'VXV-USD', 'WAN-USD', 'WBTC-USD', 'WIN-USD', 'WNCG-USD', 'WOZX-USDLINA1-USD', 'WRFOX-USD', 'WRX-USD', 'WTRX-USD', 'WWXT-USD', 'XAUT-USD', 'XCAD-USD', 'XCH-USD', 'XHV-USD', 'XLCX-USD', 'XLM-USD', 'XMR-USD', 'XNO-USD', 'XPRT-USD', 'XRP-USD', 'XVG-USD', 'XYO-USD', 'YFII-USD', 'YGG-USD', 'ZB-USD'))
  eth_df = yf.download(currency,start_date, today)
  eth_df.reset_index(inplace=True)
  # eth_df.columns

  df = eth_df[["Date", "Open"]]

  new_names = {
      "Date": "ds", 
      "Open": "y",
  }

  df.rename(columns=new_names, inplace=True)

  # df.tail()

  # plot the open price

  x = df["ds"]
  y = df["y"]
  # st.area_chart(y)
  fig = go.Figure()

  bb=fig.add_trace(go.Scatter(x=x, y=y))
  # st.write("# History of Ethereum")

  # Set title
  fig.update_layout(
      title_text="Time series plot of currency open price",
  )
  fig2 = go.Figure(data=[go.Candlestick(x=eth_df['Date'],
                  open=eth_df['Open'],
                  high=eth_df['High'],
                  low=eth_df['Low'],
                  close=eth_df['Close'])])
  # st.write("# History of Ethereum with Candlesticks")

  fig2.update_layout(
      xaxis=dict(
          rangeselector=dict(
              buttons=list(
                  [
                      dict(count=1, label="1m", step="month", stepmode="backward"),
                      dict(count=6, label="6m", step="month", stepmode="backward"),
                      dict(count=1, label="YTD", step="year", stepmode="todate"),
                      dict(count=1, label="1y", step="year", stepmode="backward"),
                      dict(step="all"),
                  ]
              )
          ),
          rangeslider=dict(visible=True),
          type="date",
      )
  )

  fig.update_layout(
      xaxis=dict(
          rangeselector=dict(
              buttons=list(
                  [
                      dict(count=1, label="1m", step="month", stepmode="backward"),
                      dict(count=6, label="6m", step="month", stepmode="backward"),
                      dict(count=1, label="YTD", step="year", stepmode="todate"),
                      dict(count=1, label="1y", step="year", stepmode="backward"),
                      dict(step="all"),
                  ]
              )
          ),
          rangeslider=dict(visible=True),
          type="date",
      )
  )

  m = Prophet(
      seasonality_mode="multiplicative")

  m.fit(df)

  future = m.make_future_dataframe(periods = 365)
  future.tail()

  forecast = m.predict(future)
  forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

  next_day = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')


  aa=plot_plotly(m, forecast)
  st.write("# Currency Price Prediction")
  st.write(aa)
  # hist_data = [m, forecast]
  # group_labels = ["History","Predicted"]
  # fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
  # st.plotly_chart(fig, use_container_width=True)
elif rad == "Custom":
  
  progress = st.progress(0)
  for i in range(0,2):
    time.sleep(0.2)
    progress.progress((i+1)*100-100)
  currency = st.selectbox("Which Currency do you want to predict",('ADA-USD', 'AERGO-USD', 'AGLD-USD', 'ALGO-USD', 'ALI2-USD', 'ALICE-USD', 'ALPACA-USD', 'ALPINE-USD', 'AMP-USD', 'AMPL-USD', 'ANY-USD', 'AQT-USD', 'AR-USD', 'ARDR-USD', 'ARPA-USD', 'ATA-USD', 'ATOM-USD', 'AURORA1-USD', 'AVAX-USD', 'BAT-USD', 'BCD-USD', 'BCH-USD', 'BEST-USD', 'BIOT-USD', 'BNANA-USD', 'BNB-USD', 'BNX-USD', 'BOBA-USD', 'BOR-USD', 'BOSON-USD', 'BRG-USD', 'BSW-USD', 'BTC-USD', 'BTCB-USD', 'BTCST-USD', 'BTS-USD', 'BUSD-USD', 'BZRX-USD', 'BZZ-USD', 'C98-USD', 'CBK-USD', 'CELO-USD', 'CHR-USD', 'CHZ-USD', 'CLV-USD', 'COMP1-USD', 'CON-USD', 'CORE-USD', 'COTI-USD', 'COVAL-USD', 'CQT-USD', 'CRE-USD', 'CRO-USD', 'CRV-USD', 'CTK-USD', 'CTSI-USD', 'CUBE-USD', 'CUDOS-USD', 'CUSD-USD', 'CVX-USD', 'CVX-USD', 'DAD-USD', 'DAG-USD', 'DAI-USD', 'DAO-USD', 'DAR-USD', 'DASH-USD', 'DCR-USD', 'DENT-USD', 'DIVI-USD', 'DNT-USD', 'DOGE-USD', 'DOT-USD', 'DPR-USD', 'DSV-USD', 'EFI-USD', 'EGG-USD', 'ELF-USD', 'ENJ-USD', 'ENS-USD', 'EPS1-USD', 'ERN-USD', 'ETC-USD', 'ETH-USD', 'EUM-USD', 'FARM-USD', 'FET-USD', 'FIDA-USD', 'FIL-USD', 'FLM-USD', 'FORTH-USD', 'FRTS-USD', 'FTT-USD', 'FX-USD', 'GALA-USD', 'GMT1-USD', 'GMT3-USD', 'GTC2-USD', 'GUSD-USD', 'HBTC-USD', 'HERO1-USD', 'HEX-USD', 'HI-USD', 'HNS-USD', 'HT-USD', 'HUM-USD', 'HUNT-USD', 'HYDRA-USD', 'ICP-USD', 'INJ-USD', 'IRIS-USD', 'JASMY-USD', 'JILL-USD', 'JOE-USD', 'KDA-USD', 'KMD-USD', 'KP3R-USD', 'KSN-USD', 'LDO-USD', 'LEO-USD', 'LINK-USD', 'LOKA-USD', 'LOOM-USD', 'LRC-USD', 'LSK-USD', 'LTC-USD', 'LTO-USD', 'LUNA1-USD', 'LYXE-USD', 'MANA-USD', 'MATIC-USD', 'MBOX-USD', 'MC-USD', 'MDX1-USD', 'MED-USD', 'METIS-USD', 'MFT-USD', 'MINA-USD', 'MLK-USD', 'MNW-USD', 'MOB-USD', 'MOC-USD', 'MOVR-USD', 'MPL-USD', 'MTL-USD', 'MVIXY-USD', 'MVL-USD', 'MX-USD', 'MXC-USD', 'NEAR-USD', 'NEO-USD', 'NEXO-USD', 'NOIA-USD', 'NU-USD', 'OGN-USD', 'OKB-USD', 'ONE1-USD', 'ONG1-USD', 'ONUS-USD', 'ORBS-USD', 'ORC-USD', 'OSMO-USD', 'PCL-USD', 'PEAK-USD', 'PEOPLE-USD', 'PERP-USD', 'PHA-USD', 'PLTC-USD', 'POWR-USD', 'PRE-USD', 'PUNDIX-USD', 'PYR-USD', 'QC-USD', 'QNT-USD', 'QUICK-USD', 'RAY-USD', 'REQ-USD', 'RFR-USD', 'RGT-USD', 'RISE1-USD', 'ROOK-USD', 'RSR-USD', 'SDAO-USD', 'SE SFP-USD', 'SHIB-USD', 'SLP-USD', 'SNT-USD', 'SOL-USD', 'SOUL-USD', 'SOV-USD', 'SPS-USD', 'STETH-USD', 'STMX-USD', 'SUPER1-USD', 'SURE-USD', 'TAVA-USD', 'TITAN-USD', 'TKO-USD', 'TLM-USD', 'TLOS-USD', 'TRAC-USD', 'TRIBE-USD', 'TROY-USD', 'TRX-USD', 'TUSD-USD', 'TVK-USD', 'UFO2-USD', 'UNI1-USD', 'UOS-USD', 'UPP-USD', 'UQC-USD', 'USDC-USD', 'USDN-USD', 'USDP-USD', 'USDT-USD', 'USDX2-USD', 'UST-USD', 'VELO-USD', 'VERI-USD', 'VET-USD', 'VRA-USD', 'VRSC-USD', 'VTHO-USD', 'VXV-USD', 'WAN-USD', 'WBTC-USD', 'WIN-USD', 'WNCG-USD', 'WOZX-USDLINA1-USD', 'WRFOX-USD', 'WRX-USD', 'WTRX-USD', 'WWXT-USD', 'XAUT-USD', 'XCAD-USD', 'XCH-USD', 'XHV-USD', 'XLCX-USD', 'XLM-USD', 'XMR-USD', 'XNO-USD', 'XPRT-USD', 'XRP-USD', 'XVG-USD', 'XYO-USD', 'YFII-USD', 'YGG-USD', 'ZB-USD'))
  eth_df = yf.download(currency,start_date, today)
  eth_df.reset_index(inplace=True)
  # eth_df.columns

  df = eth_df[["Date", "Open"]]

  new_names = {
      "Date": "ds", 
      "Open": "y",
  }

  df.rename(columns=new_names, inplace=True)

  # df.tail()

  # plot the open price

  x = df["ds"]
  y = df["y"]
  # st.area_chart(y)
  fig = go.Figure()

  bb=fig.add_trace(go.Scatter(x=x, y=y))
  # st.write("# History of Ethereum")

  # Set title
  fig.update_layout(
      title_text="Time series plot of currency Open Price",
  )
  fig2 = go.Figure(data=[go.Candlestick(x=eth_df['Date'],
                  open=eth_df['Open'],
                  high=eth_df['High'],
                  low=eth_df['Low'],
                  close=eth_df['Close'])])
  # st.write("# History of Ethereum with Candlesticks")

  fig2.update_layout(
      xaxis=dict(
          rangeselector=dict(
              buttons=list(
                  [
                      dict(count=1, label="1m", step="month", stepmode="backward"),
                      dict(count=6, label="6m", step="month", stepmode="backward"),
                      dict(count=1, label="YTD", step="year", stepmode="todate"),
                      dict(count=1, label="1y", step="year", stepmode="backward"),
                      dict(step="all"),
                  ]
              )
          ),
          rangeslider=dict(visible=True),
          type="date",
      )
  )

  fig.update_layout(
      xaxis=dict(
          rangeselector=dict(
              buttons=list(
                  [
                      dict(count=1, label="1m", step="month", stepmode="backward"),
                      dict(count=6, label="6m", step="month", stepmode="backward"),
                      dict(count=1, label="YTD", step="year", stepmode="todate"),
                      dict(count=1, label="1y", step="year", stepmode="backward"),
                      dict(step="all"),
                  ]
              )
          ),
          rangeslider=dict(visible=True),
          type="date",
      )
  )

  m = Prophet(
      seasonality_mode="multiplicative")

  m.fit(df)

  future = m.make_future_dataframe(periods = 365)
  future.tail()

  forecast = m.predict(future)
  forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

  next_day = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')


  aa=plot_plotly(m, forecast)
  
  
  strdate=st.date_input("Enter Date")
  #datetimeobj=datetime.strptime(strdate,"%y-%m-%d")
  #
  for i in forecast.index:
      if(strdate ==forecast['ds'][i]):
        st.write("## Currency Price on",forecast['ds'][i],"is",forecast['yhat'][i],"United States Dollar","and",forecast['yhat'][i]*76.1,"in Indian Rupee")
      # j=0
      # if st.checkbox("Show Center Information data"):
      #     for i in forecast.index:
      #       st.write(forecast['ds'][i])
      #       st.write(forecast['yhat'][i])
      #       strdate += timedelta(days=1)
      #       j+=1
      #       if(j>10):
      #         break
else:
  st.balloons()
  progress = st.progress(0)
  for i in range(0,2):
    time.sleep(0.2)
    progress.progress((i+1)*100-100)
  
  st.success("Thank you for knowing about us")
  
  st.write("### We are Computer Science Undergraduates from Saveetha Engineering College")
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: gray;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with Streamlit by <br>SYV</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
