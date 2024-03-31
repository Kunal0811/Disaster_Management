import streamlit as st
import mysql.connector

# Function to connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='081104',
        database='user'
    )

# Login Page
def login_page():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Check credentials in the database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        if user:
            st.success(f"Welcome, {user[1]}")
        else:
            st.error("Invalid email or password")
        db.close()

# Signup Page
def signup_page():
    st.title("Sign Up")
    email = st.text_input("Email")
    name = st.text_input("Name")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        # Insert new user into the database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        db.commit()
        st.success("Sign up successful. Please log in.")
        db.close()
        

def app():
    page = st.radio("Navigation", ["Login", "Sign Up"])
    if page == "Login":
        login_page()
    else:
        signup_page()

if __name__ == "__main__":
    app()
