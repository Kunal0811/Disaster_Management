import streamlit as st
from click import style
import time
import dailyalerts
import requests
import xml.etree.ElementTree as ET

st.set_page_config(layout="wide", page_icon="disbg.jpg", page_title="Main")

def set_background_image(image_url):
    # Define the CSS styles
    background_style = """
        <style>
            body {
                background-image: url('https://unblast.com/wp-content/uploads/2021/01/Space-Background-Images.jpg'); /* Replace with your image URL */
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
        </style>
    """

    # Inject the CSS styles into the streamlit app
    st.markdown(styles, unsafe_allow_html=True)

# Main function to run the app
def run():

    set_background_image("bg69.jpg")

def fetch_disaster_alerts():
    url = "https://gdacs.org/xml/rss.xml"
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

# Function to parse disaster alerts from XML data
def parse_disaster_alerts(xml_data):
    alerts = []
    root = ET.fromstring(xml_data)
    for item in root.iter('item'):
        alert = {}
        alert['title'] = item.find('title').text
        alert['description'] = item.find('description').text
        # You can parse other fields such as date, location, etc. as needed
        alerts.append(alert)
    return alerts


def app():

    st.markdown("<h1 style='text-align: center; color: white; font-size: 60px;'>DISASTER RELIEF PORTAL</h1>",
                unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("Alert")
    # Fetch disaster alerts from GDACS RSS feed
    xml_data = fetch_disaster_alerts()
    if xml_data:
        # Parse XML data and extract disaster alerts
        alerts = parse_disaster_alerts(xml_data)
        # Create a string with all the alerts
        alerts_str = "\t\t\t".join([f"{alert['title']}" for alert in alerts])
        # Display the scrolling animation
        st.markdown(f"""<div style="width: 100%; white-space: nowrap; overflow: hidden;">
            <marquee behavior="scroll" direction="left" style="display: inline-block;">{alerts_str}</marquee>
        </div>""", unsafe_allow_html=True)
    else:
        st.error("Failed to fetch disaster alerts from GDACS.")
    st.markdown("---")

    st.write("Welcome to our **Disaster Relief Portal** ! "
            "As the apex body for disaster management in World,we are committed to safeguarding "
            "lives, minimizing damage,and building a resilient world.")
    st.subheader("**Our Vision:**")
    st.write("**Prevention, Mitigation, Preparedness, and Response:**")
    st.write("We envision an ethos where all stakeholders work together to prevent, mitigate, prepare for and respond"
             "effectively to disasters.")
    st.write("**Technology-Driven Approach:**")
    st.write("We adopt a technology-driven, multi-hazard, and multisectoral strategy to create a safer and disaster-resilient World.")

    import subprocess
    st.divider()
    st.header("Types of Disaster")
    col1, col2 = st.columns(2)
    col1.subheader("Natural Disaster")
    st.markdown(
        """
            <style>
                /* Button width */
                div[data-testid="stButton"] button {
                    background-color: #4CAF50; /* Green */
                    border: white;
                    color: white;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 100px;
                    padding: 50px 90px; /* Adjust padding to make the button bigger */
                    margin: 10px; /* Add margin for spacing between buttons */
                    cursor: pointer;
                    border-radius: 10px;
                    width: 300px;
                    transition: all 0.4s; /* Apply transition effect to all properties */
                }
                div[data-testid="stButton"] button:hover {
                    background color: linear-gradient(135deg, #45a049, #4CAF50);
                    transform: scale(1.1); /* Scale up the button size when hovered */
                }
            </style>
        """,
        unsafe_allow_html=True)
    if col1.button("Cyclone"):
        output = subprocess.run(["streamlit", "run", "cyclone.py"], capture_output=True, text=True)
        st.markdown(output.stdout, unsafe_allow_html=True)
    if col1.button("Earthquake"):
        output = subprocess.run(["streamlit", "run", "earthquake.py"], capture_output=True, text=True)
        st.markdown(output.stdout, unsafe_allow_html=True)
    if col1.button("Flood"):
        output = subprocess.run(["streamlit", "run", "flood.py"], capture_output=True, text=True)
        st.markdown(output.stdout, unsafe_allow_html=True)


    col2.subheader("Man-made Disasters")
    if col2.button("Chemical"):
        output = subprocess.run(["streamlit", "run", "chemical.py"], capture_output=True, text=True)
        st.markdown(output.stdout, unsafe_allow_html=True)
    if col2.button("Nuclear"):
        st.write("Content for Nuclear Disasters")
    if col2.button("Biological"):
        st.write("Content for Biological Disasters")


# Add HTML/CSS to set background image
st.markdown(
    """
    <style>
    body {
        background-image: url('bg69.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        }
    </style>
    """,
    unsafe_allow_html=True
)









