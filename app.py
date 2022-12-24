import streamlit as st

st.header('This is the project for Bit Academy')
# st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')

# First task
testim = st.text_input('This is the text input')
st.text(testim)

# This is just to hide the header and the footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
