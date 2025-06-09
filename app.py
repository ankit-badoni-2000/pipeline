import streamlit as st
from src.logic import greet_user

st.title("Streamlit CI/CD Example")
name = st.text_input("Enter your name")

if name:
    st.write(greet_user(name))
