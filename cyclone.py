import streamlit as st
import requests
import xml.etree.ElementTree as ET
import folium
from streamlit_folium import folium_static
import time
import pandas as pd
import re


def fetch_cyclone_data():
    url = "https://www.gdacs.org/XML/RSS.xml"
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

# Function to parse XML response and extract cyclone data
def parse_cyclone_data(xml_content):
    cyclone_data = []
    root = ET.fromstring(xml_content)
    for item in root.findall('.//item'):
        name = item.find('title').text if item.find('title') is not None else ""
        description = item.find('description').text if item.find('description') is not None else ""
        lat_lon_match = re.search(r"(-?\d+\.\d+),\s*(-?\d+\.\d+)", description)
        if lat_lon_match:
            latitude = float(lat_lon_match.group(1))
            longitude = float(lat_lon_match.group(2))
        else:
            continue
        intensity = item.find('.//intensity').text if item.find('.//intensity') is not None else ""
        cyclone = {
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'intensity': intensity
        }
        cyclone_data.append(cyclone)
    return cyclone_data

# Function to create a map with cyclone data using Folium
def create_cyclone_map(cyclone_data):
    m = folium.Map(location=[0, 0], zoom_start=2)
    for cyclone in cyclone_data:
        lat, lon = cyclone['latitude'], cyclone['longitude']
        folium.Marker(location=[lat, lon], popup=cyclone['name']).add_to(m)
    return m

st.set_page_config(layout="wide")
# Title and Short Description
st.title("Cyclones: Be Prepared, Stay Safe")
st.write("This page provides information about cyclones and essential safety measures to take before, during, and after a cyclone event.")


st.image('cyclone.jpg', caption='Cyclone', use_column_width=True)

# Information about Cyclones
st.header("What are Cyclones?")
cyclone_info = """
Cyclones are intense rotating storm systems formed over warm tropical waters. They are characterized by strong winds, heavy rain, and storm surges that can cause significant damage and loss of life. 
"""
st.markdown(cyclone_info)

# Safety Measures - Heading
st.header("Cyclone Safety Measures")
st.subheader("Before a Cyclone:")
precautions_before = [
    "Stay informed: Monitor weather reports and warnings issued by official authorities.",
    "Prepare an emergency kit: Include non-perishable food, water, first-aid supplies, medications, flashlight, radio, etc.",
    "Secure your home: Trim trees, board up windows, and bring in outdoor furniture.",
    "Develop an evacuation plan: Identify a safe evacuation route and shelter location.",
    "Fill bathtubs and containers with clean water in case of disruptions."
]
st.markdown("\n".join(f"- {point}" for point in precautions_before))

# Safety Measures - During a Cyclone
st.subheader("During a Cyclone:")
precautions_during = [
    "Evacuate if instructed to do so by authorities.",
    "Stay indoors in a safe room away from windows and doors.",
    "Turn off utilities if flooding is a danger.",
    "Listen to the radio or local broadcasts for updates.",
    "Do not go outside until authorities declare it safe."
]
st.markdown("\n".join(f"- {point}" for point in precautions_during))

# Safety Measures - After a Cyclone
st.subheader("After a Cyclone:")
precautions_after = [
    "Stay away from downed power lines and damaged buildings.",
    "Be cautious of floodwaters and potential contamination.",
    "Report any injuries or damages to emergency services.",
    "Help others in need if it is safe to do so.",
    "Follow instructions from authorities regarding recovery efforts."
]
st.markdown("\n".join(f"- {point}" for point in precautions_after))

# Dos and Don'ts
st.header("Dos and Don'ts During a Cyclone")
dos_donts = {
    "Dos": [
        "Stay informed and listen to official warnings.",
        "Evacuate if instructed to do so.",
        "Secure your belongings and prepare an emergency kit.",
        "Stay indoors in a safe room during the storm.",
        "Help others in need if it is safe to do so."
    ],
    "Don'ts": [
        "Ignore official warnings or evacuation orders.",
        "Go outside during the storm surge or high winds.",
        "Drive through flooded areas.",
        "Use candles or open flames during power outages.",
        "Spread rumors or panic."
    ]
}

st.subheader("Dos:")
st.markdown("\n".join(f"- {point}" for point in dos_donts["Dos"]))

st.subheader("Don'ts:")
st.markdown("\n".join(f"- {point}" for point in dos_donts["Don'ts"]))

st.subheader("Classification of Disturbances Based on Wind Speed:")

data = {'Type of Disturbances': ['Low Pressure', 'Depression', 'Deep Depression','Cyclonic Storm','Severe Cyclonic Storm','Super Cyclone'],
        'Wind Speed in Km/h': ['Less than 31','31-49','49-61','61-88','88-117','More than 221'],
        'Wind Speed in Knots': ['Less than 17', '17-27', '27-33','33-47','47-63','More than 120']}

# Create table using markdown
table = '|  Type of Disturbances  |  Wind Speed in Km/h  |  Wind Speed in Knots  |\n| ---       | --- | ---     |\n'
for idx, name in enumerate(data['Type of Disturbances']):
    table += f'| {name}   | {data["Wind Speed in Km/h"][idx]} | {data["Wind Speed in Knots"][idx]}    |\n'

# Display the table in the Streamlit app
st.markdown(table, unsafe_allow_html=True)

# Display th
st.title("Cyclone Disaster Map")
xml_content = fetch_cyclone_data()
if xml_content:
    cyclone_data = parse_cyclone_data(xml_content)
    cyclone_map = create_cyclone_map(cyclone_data)
    # Convert Folium map to HTML and embed it into Streamlit using iframe
    cyclone_map.save("map.html")
    st.markdown('<iframe src="map.html" width="1000" height="500"></iframe>', unsafe_allow_html=True)
else:
    st.error("Failed to fetch cyclone data. Please try again later.")


VIDEO_URL = "https://youtu.be/FxF8fPdtGao"
st.video(VIDEO_URL)

# Conclusion
st.subheader("Stay Prepared, Stay Safe!")
conclusion = """
By being informed and taking necessary precautions, you can significantly reduce the risks associated with cyclones. Remember, preparedness is key to staying safe during these natural disasters."""
st.markdown(conclusion)