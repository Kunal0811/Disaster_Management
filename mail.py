import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="081104",
    database="user"
)
cursor = conn.cursor()

# Query email addresses from MySQL
cursor.execute("SELECT email FROM users")
emails = cursor.fetchall()

# Compose email
subject = "Notification"
body = "This is a notification message."

# Setup SMTP server
smtp_server = "smtp.gmail.com"
port = 587  # Gmail's SMTP server port
sender_email = "kunalauti@gmail.com"
password = "Kunal041108"

# Create message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send email to each recipient
for email in emails:
    recipient_email = email[0]
    msg['To'] = recipient_email
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

# Close MySQL connection
cursor.close()
conn.close()
