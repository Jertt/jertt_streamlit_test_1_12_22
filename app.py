import streamlit as st

st.header('This is the project for Bit Academy')
# st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')

# First task
mainString = st.text_input('This is the text input')
# st.text(mainString)
b = None

def convert_list(mainString):
    varDuo = mainString.split()
    return varDuo

if st.button("Return List"):
    b = convert_list(mainString)
    st.write(b)

# Declare a function called “convert_list”  that takes this string and returns a list of words from this string. (hint: you can use .split() method ). 
# Connect this function with a button called “Return List”. When you press this button list of words is printed on streamlit.
# (hint: you can use st.write())


def convert_upper():
    b = convert_list(mainString)
    b = [a.upper() for a in b]
    st.text(b)

if st.button("Upper"):
    convert_upper()
    # st.write(test)

# (A) Declare another function called “convert_upper” that takes the list from the function called “convert_list” and converts them to a list with all upper case.
# (hint: you need to use for loop, .upper() and .append() methods ). Connect this function to a button called “upper” that activates this function and prints te result.
# (hint: you need to use st.write()



# This is just to hide the header and the footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
