import streamlit as st
import time
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Caching demonstration")

st.button("Test cache")

st.subheader("@st.cache_data")
@st.cache_data #decorator to cache function output based on input parameters/function body.
def cache_this_function():
    time.sleep(4)
    out = "I am done running"
    return out

output = cache_this_function()
st.write(output)

st.subheader("@st.cache_resource")
@st.cache_resource #decorator to cache resources like models, database connections, etc.
def cache_this_model():
     time.sleep(4)
     x = np.array([1,2,3,4,5,6,7]).reshape(-1, 1)
     y = np.array([1,2,3,4,5,6,7])
     regressor = LinearRegression()
     regressor.fit(x, y)
     return regressor

model = cache_this_model()
y_pred = model.predict(np.array([9]).reshape(-1, 1))
st.write(f"Prediction for 8 is {y_pred[0]}")