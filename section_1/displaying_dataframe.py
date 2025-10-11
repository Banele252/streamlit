import streamlit as st
import pandas as pd

df = pd.read_csv("data/sample.csv")
print(df)
st.dataframe(df)
st.write(df)
st.table(df)