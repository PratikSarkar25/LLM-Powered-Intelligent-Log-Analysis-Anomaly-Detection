import streamlit as st
import pandas as pd
from parser import load_logs
from anomaly import detect_anomalies
from rag_engine import answer_query
import plotly.express as px

st.set_page_config(page_title='Enterprise Log Analyzer', layout='wide')
st.title('Enterprise AI Log Analyzer')

file = st.file_uploader('Upload CSV logs', type=['csv'])
if file:
    df = pd.read_csv(file)
else:
    df = load_logs()

st.subheader('Logs')
st.dataframe(df, use_container_width=True)

st.subheader('Severity Counts')
fig = px.histogram(df, x='level')
st.plotly_chart(fig, use_container_width=True)

st.subheader('Detected Issues')
for x in detect_anomalies(df):
    st.warning(x)

st.subheader('Ask the Logs')
q = st.text_input('Example: Why did payroll fail today?')
if st.button('Analyze') and q:
    with st.spinner('Thinking...'):
        ans = answer_query(q)
    st.write(ans)