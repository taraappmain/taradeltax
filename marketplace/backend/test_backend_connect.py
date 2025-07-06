import streamlit as st
import requests

st.title("Tara Backend API Test")

try:
    response = requests.get("http://127.0.0.1:8000/")
    response.raise_for_status()
    st.json(response.json())
except requests.exceptions.RequestException as e:
    st.error(f"Error connecting to backend: {e}")

