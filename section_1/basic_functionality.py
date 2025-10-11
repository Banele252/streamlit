import streamlit as st
import pandas as pd

# Give your app a title
st.title("Hello, Streamlit!")

# Header
st.header("Welcome to my first Streamlit app")
# Subheader
st.subheader("This is a subheader")
# Markdown 
st.markdown("This is a **markdown** text with _italic_ and **bold** formatting.")
st.markdown("You can also create lists:\n\n- Item 1\n- Item 2\n- Item 3")
st.markdown("And [links](https://streamlit.io) too!")

#Caption
st.caption("This is a caption text.")

#Code block
code = '''def hello_world():
          print("Hello, World!")'''

st.code(code, language='python')

# Prefformatted text
st.text("This is preformatted text.\n    It preserves spaces and line breaks.")

#Latex
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.latex(r''' \int_a^b f(x)dx = F(b) - F(a) ''')
st.latex(r''' \frac{d}{dx}e^x = e^x ''')

# Divider 
st.text("Text above the divider")
st.divider()
st.text("Text below the divider")

# st.write
st.write("This is a simple text using st.write")
st.write(12345)
