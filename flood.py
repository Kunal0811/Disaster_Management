import streamlit as st

st.set_page_config(layout="wide")
st.title("Floods: Surviving Nature's Deluge")
st.write("This page provides information about floods and essential safety measures to take before, during, and after a flood event.")

st.image('flood.jpg', caption='Flood')

# Information about Floods
st.header("What are Floods?")
flood_info = """
Floods are natural disasters characterized by an overflow of water onto normally dry land. They can result from heavy rainfall, river overflow, storm surges, or dam failures. Floods can cause extensive damage to property, infrastructure, and pose significant risks to human life.
"""
st.markdown(flood_info)

# Safety Measures - Heading
st.header("Flood Safety Measures")
st.subheader("Before a Flood:")
precautions_before = [
    "Stay Informed: Monitor weather forecasts and flood warnings issued by local authorities.",
    "Create an Emergency Plan: Establish evacuation routes and designate meeting points for family members.",
    "Prepare an Emergency Kit: Include essential items such as water, non-perishable food, medications, flashlight, and batteries.",
    "Protect Valuables: Elevate important documents, valuables, and electrical appliances to prevent water damage.",
    "Secure Your Home: Seal cracks in walls, install check valves in sewer traps, and ensure sump pumps are working.",
]
st.markdown("\n".join(f"- {point}" for point in precautions_before))

# Safety Measures - During a Flood
st.subheader("During a Flood:")
precautions_during = [
    "Evacuate if Advised: Follow evacuation orders issued by local authorities and move to higher ground if necessary.",
    "Avoid Flooded Areas: Stay away from floodwaters, as they can be fast-moving and contain debris, pollutants, and hidden dangers.",
    "Turn Off Utilities: Switch off gas, electricity, and water mains to prevent accidents and damage.",
    "Listen for Updates: Stay tuned to radio broadcasts or official channels for updates and instructions.",
    "Seek Shelter: Move to the highest level of your home or a designated shelter if evacuation is not possible.",
]
st.markdown("\n".join(f"- {point}" for point in precautions_during))

# Safety Measures - After a Flood
st.subheader("After a Flood:")
precautions_after = [
    "Wait for Clearance: Wait for authorities to declare it safe before returning to your home or affected area.",
    "Assess Damage: Inspect your property for damage and take photographs for insurance claims.",
    "Avoid Floodwater Contact: Avoid contact with floodwaters due to contamination risks.",
    "Use Caution: Be cautious of damaged roads, bridges, and infrastructure.",
    "Seek Assistance: Contact emergency services if you require assistance or encounter hazards.",
]
st.markdown("\n".join(f"- {point}" for point in precautions_after))

# Dos and Don'ts
st.header("Dos and Don'ts During a Flood")
dos_donts = {
    "Dos": [
        "Follow evacuation orders promptly.",
        "Stay informed about flood developments.",
        "Ensure utilities are turned off if evacuating.",
        "Seek higher ground and shelter if trapped.",
        "Assist others in need if it is safe to do so.",
    ],
    "Don'ts": [
        "Do not walk, swim, or drive through floodwaters.",
        "Avoid contact with floodwater due to contamination risks.",
        "Do not return home until authorities declare it safe.",
        "Do not touch electrical equipment if wet or standing in water.",
        "Avoid downed power lines and report them to authorities.",
    ]
}

st.subheader("Dos:")
st.markdown("\n".join(f"- {point}" for point in dos_donts["Dos"]))

st.subheader("Don'ts:")
st.markdown("\n".join(f"- {point}" for point in dos_donts["Don'ts"]))

VIDEO_URL = "https://youtu.be/ivUKLr8q4sE"
st.video(VIDEO_URL)

conclusion = """
In conclusion, floods are natural disasters that can have devastating impacts on communities. Preparedness, vigilance, and adherence to safety measures are essential for mitigating risks and ensuring safety during flood events."""
st.markdown(conclusion)