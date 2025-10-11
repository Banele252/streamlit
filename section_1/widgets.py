import streamlit as st
import pandas as pd
df = pd.read_csv("data/sample.csv")

primary_btn = st.button("Primary Button", type="primary")
secondary_btn = st.button("Secondary Button", type="secondary")

if primary_btn:
    st.write("You clicked the Primary Button!")
if secondary_btn:
    st.write("You clicked the Secondary Button!")


#checkbox
st.divider()

checkbox = st.checkbox("Remember me")
if checkbox:
    st.write("You remembered me!")
else:
    st.write("You didn't remember me!")

# radio button
st.divider()

radio = st.radio("Select a columnt", options=df.columns[1:], index=0)
st.write(f"You selected: {radio}")


# Selectbox
st.divider()

selectbox = st.selectbox("Select a column", options=df.columns[1:], index=0)
st.write(f"You selected: {selectbox}")

#Multiselect
st.divider()
multiselect = st.multiselect("Select columns", options=df.columns[1:], default=df.columns[1], max_selections=2)
st.write(f"You selected: {multiselect}")

#Slider
st.divider()
slider = st.slider("Select a range of values", min_value = 0, max_value = 100, step = 5)
st.write(f"You selected: {slider}")

#Text input
st.divider()
text_input = st.text_input("Enter your name", value="John Doe")
st.write(f"Hello, {text_input}!")

#Text area
st.divider()
text_area = st.text_area("Enter a message", value="Hello, Streamlit!", height=200)
st.write(f"You wrote: {text_area}")

