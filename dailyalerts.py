import streamlit as st
import feedparser
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to fetch disaster alerts from GDACS RSS feed
def fetch_disaster_alerts():
    url = "https://gdacs.org/xml/rss.xml"
    feed = feedparser.parse(url)
    return feed.entries

# Function to fetch emails from MySQL database
def fetch_emails_from_database():
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="081104",
        database="user"
    )
    cursor = conn.cursor()

    # Fetch emails from database
    cursor.execute("SELECT email FROM users")
    emails = [row[0] for row in cursor.fetchall()]

    # Close database connection
    cursor.close()
    conn.close()

    return emails

# Function to send email
def send_email(subject, body, to_email):
    sender_email = "kunalauti062@gmail.com"
    sender_password = "wald hmtp cafz nrtz"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Connect to SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())

# Main function to display the app
def app():
    st.title("Disaster Alerts")


    # Fetch disaster alerts
    alerts = fetch_disaster_alerts()

    # Display alerts
    if alerts:
        st.markdown("---")
        for alert in alerts:
            st.markdown(f"## :warning: {alert.title}")
            st.markdown(f"**Summary:** {alert.summary}")
            st.markdown(f"[Read more]({alert.link})")
            st.markdown("---")
    else:
        st.error("No disaster alerts found")

    # Fetch disaster alerts

    # Fetch emails from database
    emails = fetch_emails_from_database()

    # Send alerts to emails
    if alerts and emails:
        for alert in alerts:
            for email in emails:
                send_email(alert.title, alert.summary, email)
    else:
        st.error("No disaster alerts found or no emails available in the database")

    st.success("Disaster alerts sent successfully to all subscribers!")

    

if __name__ == "__main__":
    app()
