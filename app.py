import streamlit as st

st.header('This is the project for Bit Academy')
# st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')

testim = st.text_input('This is the text input')
st.text(testim)
