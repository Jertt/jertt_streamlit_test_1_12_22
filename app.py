import streamlit as st

st.header('This is the project for Bit Academy')

# Task 1
mainString = st.text_input('This is the text input')

b = None

def convert_list(mainString):
    varDuo = mainString.split()
    return varDuo

if st.button("Return List"):
    b = convert_list(mainString)
    st.write(b)

# Task 3
def convert_upper():
    b = convert_list(mainString)
    b = [a.upper() for a in b]
    return b

if st.button("Upper"):
    c = convert_upper()
    st.write(c)


# Task 4
def count():
    lista = convert_list(mainString)
    lista = len(lista)
    return lista

if st.button("print_count"):
    d = count()
    st.write("This list has ", d, " elements")


# This is just to hide the header and the footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
