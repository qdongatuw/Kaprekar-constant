import streamlit as st

def calculation(n):
    s = list(str(n))
    big = ''.join(sorted(s, reverse=True))
    small = ''.join(sorted(s))
    
    


st.sidebar.header('Hi Mason!')
st.title("Kaprekar's constant")

ini_numer = st.sidebar.number_input('Input a number:', value=2048)
