import streamlit as st

with st.form("reservation_form"):
# Order message after creating the form
    st.header("Restaurant Reservation Form")
# Appitizers input filed (dropdown)
    appetizers = st.selectbox("Appetizer", options=["Salad", "Soup", "Bruschetta"], index=2)

# Main course input field (dropdown)
    Maiin = st.selectbox("Main cousrse", options=["Salad", "Soup", "Bruschetta"])
# Dessert input field (dropdown)
    Dessert = st.selectbox("Dessert", options=["Salad", "Soup", "Bruschetta"])
# Check box bringing your own wine
    wine = st.checkbox("Bringing your own wine", value=True)
# date input field for reservation date
    date = st.date_input("Reservation Date")

# time input field for reservation time
    time = st.time_input("Reservation Time")

# Any allergies input field (text area)
    allergies = st.text_area("Allergies or special requests", placeholder="Please list any allergies or special requests here.",height=100)
# Submit button
    submitted = st.form_submit_button("Submit Reservation")

if submitted:
        st.success("Reservation submitted successfully!") # Display success message
        st.write("### Reservation Details:")
        st.write(f"- **Appetizer:** {appetizers}")
        st.write(f"- **Main Course:** {Maiin}")
        st.write(f"- **Dessert:** {Dessert}")
        st.write(f"- **Bringing Wine:** {'Yes' if wine else 'No'}")
        st.write(f"- **Date:** {date}")
        st.write(f"- **Time:** {time}")
        st.write(f"- **Allergies/Special Requests:** {allergies if allergies else 'None'}")