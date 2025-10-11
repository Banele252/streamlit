import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample.csv")

#streamlit line plot
st.line_chart(df, x='year', y=["col1","col2","col3"])

#streamlit area chart
st.area_chart(df, x='year', y=["col1","col2","col3"])

#streamlit bar chart
st.bar_chart(df, x='year', y=["col1","col2","col3"])

#streamlit map
df_map = pd.read_csv("data/sample_map.csv")
st.map(df_map)

#Matplotlib
fig, axis = plt.subplots()
axis.plot(df['year'], df['col1'], label='col1') 
axis.plot(df['year'], df['col2'], label='col2')
axis.set_xlabel('Year')
axis.set_ylabel('Values')
axis.set_title('Matplotlib Line Plot')
axis.legend()
st.pyplot(fig)
