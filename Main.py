import streamlit as st
import random

#Function - getting quote
def get_quote():
    with open(f"quotes.txt", encoding="utf8") as file:
        quotes = file.readlines()
        quote_on_screen = random.choice(quotes)
    return quote_on_screen[4:]

#Button for another quote
def get_another_quote():
    if button:
        get_quote()

#Configuration of page's apperance
st.set_page_config(page_title="Hello!️", layout="wide")
m = st.markdown("""
<style>
div.stButton > button{
    background-color: rgb(204, 49, 49);
    color: rgb(256,256,256)
}
</style>""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Hello!❤️</h1>", unsafe_allow_html=True)

st.write("""
**Get organized!**
**Set** your goals, **plan** your days and **track** your habits!
""",unsafe_allow_html=True)

st.image('https://cdn.pixabay.com/photo/2018/03/01/05/46/business-3189797_960_720.png', use_column_width=True)

st.sidebar.markdown("# Stay motivated!")
st.sidebar.markdown('### Quote for you:')
st.sidebar.write(get_quote())
button = st.sidebar.button('Get another quote')