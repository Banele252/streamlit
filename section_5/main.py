import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# Hash passwords and store it in the YAML file, run this once.
# hashed_pwd = stauth.Hasher.hash('12345')
# st.write(hashed_pwd)

# Create authenticator object
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create authenticator object 
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Render the login widget
authenticator.login()

# Extract authentication data
authentication_status = st.session_state.get("authentication_status")
name = st.session_state.get("name")
username = st.session_state.get("username")

# Authenticate users
if authentication_status:
    authenticator.logout()
    st.write(f'Welcome *{name}*')
    st.title('Some content')
    
    # Password reset widget (only for authenticated users)
    try:
        if authenticator.reset_password(username):
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)
    
    # Update user details (only for authenticated users)
    try:
        if authenticator.update_user_details(username):
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)
        
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

# Register new user (available to everyone)
try:
    if authenticator.register_user(pre_authorized=None):
        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
        st.success('User registered successfully')
except Exception as e:
    st.error(e)

# Forgot password widget (available to everyone)
try:
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
    if username_of_forgotten_password:
        st.success('New password sent securely')
        # Random password to be transferred to user securely
        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
    elif username_of_forgotten_password is False:
        st.error('Username not found')
except Exception as e:
    st.error(e)

# Forgot username (available to everyone)
try:
    username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
    if username_of_forgotten_username:
        st.success('Username sent securely')
        # Username to be transferred to user securely
    elif username_of_forgotten_username is False:
        st.error('Email not found')
except Exception as e:
    st.error(e)

st.write(st.session_state)