import streamlit as st
from datetime import datetime, timedelta


st.title("Advanced State Management")

# Store widget value in session state
st.subheader("Store widget value in session state")
st.number_input("enter a number",min_value = 0,max_value = 100, key = "number_input")
st.write("The number you entered is:", st.session_state["number_input"])

# Initialize widget value with session state

st.subheader("Initialize widget value with session state")
if "slider" not in st.session_state:
    st.session_state["slider"] = 5
st.slider("Select a value",min_value = 0,max_value = 10, key = "slider")
st.write("The slider value is:", st.session_state["slider"])



# Callbacks
st.subheader("Use callbacks")
# Add days callback
def add_days():
    if st.session_state["time_range"] == "7 days":
        st.session_state["end_date"] = st.session_state["start_date"] + timedelta(days=7)
    elif st.session_state["time_range"] == "28 days":
        st.session_state["end_date"] = st.session_state["start_date"] + timedelta(days=28)
    else:
        pass


def substract_days():
    if st.session_state["time_range"] == "7 days":
        st.session_state["start_date"] = st.session_state["end_date"] - timedelta(days=7)
    elif st.session_state["time_range"] == "28 days":
        st.session_state["start_date"] = st.session_state["end_date"] - timedelta(days=28)
    else:
        pass


st.markdown("#### Select your time range")

st.radio("Select a range", ["7 days", "28 days", "custom"], horizontal=True, key = "time_range",  on_change=add_days)

col1, col2, col3 = st.columns(3)

col1.date_input("Start date", key = "start_date", on_change=add_days)
col2.date_input("End date",key = "end_date", on_change=substract_days)