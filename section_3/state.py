import streamlit as st

# State management for Streamlit app
st.header("Stateful Apps")

# Display the state 
st.write("Here is the session state:")
st.write(st.session_state)
st.button("Update State")

# # Set the value of a state variab
if "key" not in st.session_state:
     st.session_state['key'] = "Initial value"

# #Set the value of a session state attribute
if "attribute" not in st.session_state:
     st.session_state.attribute = "Another state value"

# # #Read value from session state
st.write("Current value of 'key':", st.session_state['key'])
st.write("Current value of 'attribute':", st.session_state.attribute)

# # # # Update state values on button click
st.session_state['key'] = "Updated value"
st.session_state.attribute = "Updated attribute value"
st.write("State updated!")