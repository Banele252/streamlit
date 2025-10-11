import streamlit as st
import pandas as pd

# Side bar
with st.sidebar:
    st.write("This is the sidebar")
    st.button("Click me!")
    st.checkbox("Check me!")

# Columns
col1, col2,col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.button("Button 1")
with col2:
    st.header("Column 2")
    st.button("Button 2")
with col3:
    st.header("Column 3")
    st.button("Button 3")

# Tabs 
df = pd.read_csv("data/sample.csv")
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("A line chart")
    st.line_chart(df, x='year', y=["col1","col2","col3"])
with tab2:
    st.write("A bar chart")
    st.bar_chart(df, x='year', y=["col1","col2","col3"])
with tab3:
    st.write("A table")
    st.dataframe(df)

# Expander
with st.expander("See explanation"):
    st.write("""
        Here you can put in any explanation or additional information.
        This section is collapsible and can be expanded or collapsed by the user.
    """)
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)
    st.code('''import streamlit as st
    st.title("Hello, Streamlit!")''', language='python')

# Progress bar
import time
st.write("Progress bar example:")
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.05)
    progress_bar.progress(percent_complete + 1)
    
st.write("Task completed!")

# Container
with st.container():
    st.write("This is inside a container")
    st.line_chart(df, x='year', y=["col1","col2","col3"])
    st.write("You can put multiple elements inside a container.")