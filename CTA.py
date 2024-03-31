
import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
def app():
    # Usernm = []
    st.title(':red[Emergency Contacts] :telephone:')
    st.subheader('Police : 100')
    st.subheader('Ambulance : 112')
