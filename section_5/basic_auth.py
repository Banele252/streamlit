import streamlit as st

#initialize session state variables
if all(key not in st.session_state.keys() for key in ('pwd','pwd_correct','button_clicked','username')):
    st.session_state['pwd'] = ''
    st.session_state['pwd_correct'] = False
    st.session_state['button_clicked'] = False
    st.session_state['username'] = ''


# Create a function to check the password
def check_password():
    st.session_state['button_clicked'] = True
    if (st.session_state['pwd'] == st.secrets["password"])\
          and (st.session_state['username'] == st.secrets['passwords']['username']):
        st.session_state['pwd_correct'] = True
        st.session_state['pwd'] = ''
        st.session_state['username'] = ''
    else:
        st.session_state['pwd_correct'] = False

#Create a function to display the login form
def display_login_form():
    with st.form("login_form"):
        st.text_input('Username',key='username')
        st.text_input('Password',type='password', key='pwd')
        st.form_submit_button('Login', on_click=check_password)
        

if __name__ == "__main__":
    if (st.session_state['pwd_correct'] == False) and (st.session_state['button_clicked']==False):
        display_login_form()
    elif (st.session_state['pwd_correct'] == False) and (st.session_state['button_clicked']==True):
        st.error('Incorrect password or username. Please try again.')
        display_login_form()
        st.write(st.session_state)
    elif st.session_state['pwd_correct']:
        st.success('Login successful!')
        st.write('Welcome to the protected section of the app.')
    else:
        display_login_form()