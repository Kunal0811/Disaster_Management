import streamlit as st
import folium
import requests

st.set_page_config(layout="wide")
st.title("Earthquakes: Resilience Amid Earth's Tremors.")
st.write("This page provides information about earthquakes and essential safety measures to take before, during, and after an earthquake event.")

def fetch_earthquake_data():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to create a map with earthquake data using Folium
def create_earthquake_map(earthquake_data):
    m = folium.Map(location=[0, 0], zoom_start=2)
    for feature in earthquake_data['features']:
        coordinates = feature['geometry']['coordinates']
        magnitude = feature['properties']['mag']
        popup_text = f"Magnitude: {magnitude}"
        folium.Marker(location=[coordinates[1], coordinates[0]], popup=popup_text).add_to(m)
    return m

st.image('earthquake.jpg', caption='Earthquake')

# Information about Earthquakes
st.header("What are Earthquakes?")
earthquake_info = """
Earthquakes are sudden shaking or trembling of the ground caused by the movement of tectonic plates beneath the Earth's surface. They can range in intensity from mild to severe and can cause significant damage to buildings, infrastructure, and landscapes.
"""
st.markdown(earthquake_info)

# Safety Measures - Heading
st.header("Earthquake Safety Measures")
st.subheader("Before an Earthquake:")
precautions_before = [
    "Secure heavy items: Anchor heavy furniture, appliances, and objects to prevent them from toppling over.",
    "Create an emergency plan: Establish evacuation routes and meeting points for family members.",
    "Prepare an emergency kit: Include water, non-perishable food, first-aid supplies, flashlight, radio, etc.",
    "Secure your home's structure: Identify and reinforce weak points in your home's structure.",
    "Know the safe spots: Identify safe spots in each room where you can take cover during an earthquake."
]
st.markdown("\n".join(f"- {point}" for point in precautions_before))

# Safety Measures - During an Earthquake
st.subheader("During an Earthquake:")
precautions_during = [
    "Drop, Cover, and Hold On: Drop to the ground, take cover under a sturdy piece of furniture, and hold on until shaking stops.",
    "Stay indoors: Avoid going outside during the shaking to prevent injuries from falling debris.",
    "Protect your head: Use your arms to protect your head and neck from falling objects.",
    "Be prepared for aftershocks: After the initial shaking stops, be prepared for aftershocks and take cover as necessary.",
    "Listen for updates: Listen to the radio or local broadcasts for updates and instructions from authorities."
]
st.markdown("\n".join(f"- {point}" for point in precautions_during))

# Safety Measures - After an Earthquake
st.subheader("After an Earthquake:")
precautions_after = [
    "Check for injuries: Check yourself and others for injuries and provide first aid as needed.",
    "Check for damage: Assess your home and surroundings for damage and hazards.",
    "Evacuate if necessary: If your home is unsafe, evacuate to a safe location and follow emergency instructions.",
    "Use caution: Be cautious of damaged infrastructure, downed power lines, and potential gas leaks.",
    "Help others: Assist others in need if it is safe to do so and report any emergencies to authorities."
]
st.markdown("\n".join(f"- {point}" for point in precautions_after))

# Dos and Don'ts
st.header("Dos and Don'ts During an Earthquake")
dos_donts = {
    "Dos": [
        "Drop, Cover, and Hold On during shaking.",
        "Stay indoors and away from windows and heavy objects.",
        "Listen to official updates and instructions.",
        "Check for injuries and provide first aid as needed.",
        "Help others and report emergencies to authorities."
    ],
    "Don'ts": [
        "Do not use elevators during an earthquake.",
        "Do not run outside during shaking.",
        "Do not use candles or open flames after the quake.",
        "Do not spread rumors or panic.",
        "Do not re-enter damaged buildings until they are declared safe."
    ]
}

st.subheader("Dos:")
st.markdown("\n".join(f"- {point}" for point in dos_donts["Dos"]))

st.subheader("Don'ts:")
st.markdown("\n".join(f"- {point}" for point in dos_donts["Don'ts"]))

st.title("Earthquake Map")
st.write("Real-time earthquake data from the USGS Earthquake Catalog API")
earthquake_data = fetch_earthquake_data()
if earthquake_data:
    earthquake_map = create_earthquake_map(earthquake_data)
    st.write(earthquake_map._repr_html_(), unsafe_allow_html=True)
else:
    st.error("Failed to fetch earthquake data. Please try again later.")


VIDEO_URL = "https://youtu.be/17kBVfGjI8c"
st.video(VIDEO_URL)

conclusion = """
In conclusion, earthquakes are natural phenomena that can strike with little warning, causing widespread devastation. Staying informed, prepared, and vigilant is crucial to mitigating the risks and ensuring safety in earthquake-prone areas."""
st.markdown(conclusion)