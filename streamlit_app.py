import streamlit as st
import pandas as pd
import plotly.express as px
APP_TITLE = "Tesla Stock Analytics Dashboard"

st.set_page_config(page_title=APP_TITLE, layout="wide")
st.markdown('''
<style>
.block-container {padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1180px;}
[data-testid="stMetricValue"] {font-size: 1.65rem;}
.small-note {color: #5f6368; font-size: 0.92rem;}
</style>
''', unsafe_allow_html=True)


df = pd.read_csv("data/tesla_stock_sample.csv", parse_dates=["date"])
df["ma20"] = df.close.rolling(20, min_periods=1).mean()
delta = df.close.diff().fillna(0)
gain = delta.clip(lower=0).rolling(14, min_periods=1).mean()
loss = (-delta.clip(upper=0)).rolling(14, min_periods=1).mean().replace(0, 0.01)
df["rsi"] = 100 - (100 / (1 + gain / loss))
df["macd"] = df.close.ewm(span=12).mean() - df.close.ewm(span=26).mean()
st.title(APP_TITLE)
st.caption("Power BI-style view rebuilt as a deployable Streamlit dashboard.")
st.metric("Latest close", f"${df.close.iloc[-1]:.2f}", f"{df.close.iloc[-1]-df.close.iloc[-30]:.2f} vs 30 days")
st.plotly_chart(px.line(df, x="date", y=["close", "ma20"], markers=False), use_container_width=True)
st.plotly_chart(px.line(df, x="date", y=["rsi", "macd"]), use_container_width=True)
st.dataframe(df.tail(30), use_container_width=True, hide_index=True)
